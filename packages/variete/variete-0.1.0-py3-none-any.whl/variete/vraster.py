"""
Definitions for the VRaster class.

Most actual functionality is in the `vrt` module.
"""
from __future__ import annotations
from pathlib import Path
import copy
import tempfile
import rasterio as rio
from rasterio.coords import BoundingBox
from rasterio.transform import Affine
from rasterio.crs import CRS
from rasterio.windows import Window
from rasterio.warp import Resampling
import numpy as np
from typing import overload, Literal, Callable, Any, Iterable
from osgeo import gdal

from variete.vrt.vrt import VRTDataset, AnyVRTDataset, load_vrt, vrt_warp, build_vrt
from variete.vrt.raster_bands import VRTDerivedRasterBand
from variete.vrt.pixel_functions import ScalePixelFunction
from variete.vrt import pixel_functions
from variete.vrt.sources import SimpleSource
from variete import misc

# tqdm is an optional dependency and will simply raise a custom exception if it's explicitly asked for.
try:
    from tqdm import tqdm

    _has_tqdm = True
except ImportError:
    _has_tqdm = False
    # For code simplicity, a dummy tqdm class is ironically needed. This makes it so that a tqdm context can
    # always be entered (even though it doesn't do anything if tqdm is not installed)
    class tqdm:
        def __init__(
            self, total: float, disable: bool = False, smoothing: float | None = None, desc: str | None = None
        ):
            ...

        def update(self, value: Any):
            ...

        def __enter__(self):
            ...

        def __exit__(self):
            ...


class VRasterStep:
    """A VRTDataset and an associated name, for logging purposes."""
    dataset: AnyVRTDataset
    name: str

    def __init__(self, dataset: AnyVRTDataset, name: str):
        for attr in ["dataset", "name"]:
            setattr(self, attr, locals()[attr])


class VRaster:
    """
    A "Virtual Raster" containing information on how to process a raster on disk.  

    A VRaster has no data loaded in memory, other than the processing steps to take when evaluating.
    Evaluation is mainly done through the `VRaster.read()` or `VRaster.write()` functions.
    """
    # The steps list is a (largely) unordered list of steps and dependencies to the last (current) dataset
    # The last dataset (VRaster.steps[-1]) is always the current one, but no other step is required for evaluation.
    # All other steps are only to show the steps that were taken to get to the latest, and are all self-contained.
    steps: list[VRasterStep]

    def __init__(self, steps: list[VRasterStep] | None = None):
        self.steps = steps or []

    @classmethod
    def load_file(cls, filepath: str | Path):
        """
        Load a VRaster from a file.

        Parameters
        ----------
        filepath
            The filepath to a GDAL-supported dataset.
        Returns
        -------
        A newly created VRaster
        """
        step = VRasterStep(VRTDataset.from_file(filepath), name="load_file")

        return cls(steps=[step])

    def save_vrt(self, filepath: str | Path) -> list[Path]:
        """
        Save the VRaster as a VRT or a stack of VRTs.

        If the VRaster is nested (depends on more than one VRTDataset), all dependents will be saved too.

        Parameters
        ----------
        filepath
            The filepath to save the VRT. Multiple VRTs may be saved with suffixes.

        Returns
        -------
        A list of filepaths that were created (multiple in case of a nested VRaster).
        """
        if self.last.is_nested():
            return self.last.save_vrt_nested(filepath)
        else:
            self.last.save_vrt(filepath)
            return [filepath]

    def _check_compatibility(self, other: "VRaster") -> str | None:
        """Check if this VRaster is compatible with another VRaster."""
        if self.crs != other.crs:
            return f"CRS is different: {self.crs} != {other.crs}"

        if self.n_bands != other.n_bands:
            return f"Number of bands must be the same: {self.n_bands} != {other.n_bands}"

    @overload
    def read(
        self,
        band: int | list[int] | None,
        out: np.ndarray | np.ma.masked_array | None,
        window: Window | None,
        masked: Literal[True],
        **kwargs,
    ) -> np.ma.masked_array:
        ...

    @overload
    def read(
        self,
        band: int | list[int] | None,
        out: np.ndarray | np.ma.masked_array | None,
        window: Window | None,
        masked: Literal[False],
        **kwargs,
    ) -> np.ndarray:
        ...

    @overload
    def read(
        self,
        band: int | list[int] | None,
        out: np.ndarray | np.ma.masked_array | None,
        window: Window | None,
        masked: Literal[False],
        **kwargs,
    ) -> np.ndarray:
        ...

    def read(
        self,
        band: int | list[int] | None = None,
        out: np.ndarray | np.ma.masked_array | None = None,
        window: Window | None = None,
        masked: bool = False,
        **kwargs,
    ) -> np.ndarray | np.ma.masked_array:
        """
        Read the contents of a VRaster into memory.

        Parameters
        ----------
        band
            A band index or a list of indices to load. Defaults to all bands.
        out
            Optional: The destination array to read to.
        window
            Optional: Read only a part of the VRaster (see the rasterio Window documentation)
        masked
            Return a masked array where all nodata values are masked.
        **kwargs
            Optional keyword arguments to supply the rio.DatasetReader.read method.

        Returns
        -------
        A numpy array of shape (bands, height, width) or a numpy masked_array
        """
        with tempfile.TemporaryDirectory() as temp_dir:
            filepath = self.last.to_tempfiles(temp_dir)[1]

            with rio.open(filepath) as raster:
                return raster.read(band, out=out, masked=masked, window=window, **kwargs)

    def write(
        self,
        filepath: Path | str,
        format: str | None = None,
        tiled: bool | None = None,
        compress: str = "deflate",
        predictor: Literal[1] | Literal[2] | Literal[3] | None = None,
        zlevel: int | str | None = None,
        creation_options: dict[str, str] | None = None,
        progress: bool = False,
        callback: Callable[float, Any, Any] | None = None,
    ) -> None:
        """
        Write the VRaster to a file.

        Parameters
        ----------
        filepath
            The output filepath to write the file.
        format
            The output format (e.g. "GTiff"). If not given, the format is inferred from the filename.
        tiled
            Whether to write the blocks in tiles (True) or in strips (False)
        compress
            What compression algorithm to use.
        predictor
            Which compression predictor to use (only valid in some compression schemes).
        zlevel
            The level of compression to use. For deflate, valid numbers range between 1 and 12
        creation_options
            Other creation options to provide to GDAL as a {key: value} dictionary
        progress
            Whether to show a tqdm progress bar. tqdm needs to be installed for this to work.
        callback
            A callback function for the writer that takes three positional arguments.
            The first argument is the progress, ranging from 0-1.

        Raises
        ------
        AssertionError
            If any requirement for file creation is not filled.
        ValueError
            If the provided arguments are incompatible.
        """
        filepath = Path(filepath)

        if not filepath.parent.is_dir():
            raise AssertionError("Filepath parent directory does not exist")

        if progress and callback is not None:
            raise ValueError("'progress' needs to be False if 'callback' is used")

        if progress and not _has_tqdm:
            raise ValueError("tqdm is required for 'progress=True'. For pip, use 'pip install tqdm'.")

        if creation_options is None:
            creation_options = {}

        lowercase_keys = [key.lower() for key in creation_options]

        for key, value in [("COMPRESS", compress), ("TILED", tiled), ("PREDICTOR", predictor), ("ZLEVEL", zlevel)]:
            if key.lower() in lowercase_keys or value is None:
                continue

            creation_options[key] = value

        # Always initialize a tqdm context, because it's easier with the context manager..
        with tempfile.TemporaryDirectory() as temp_dir, tqdm(
            total=100, disable=(not progress), smoothing=0.1, desc=f"Writing {filepath.name}"
        ) as progress_bar:
            _, vrt_path = self.last.to_tempfiles(temp_dir=temp_dir)

            if progress:
                # This callback function will scale 0-1 to 0-100 and only show integer increments.
                prev = 0.0

                def callback(value, *_):
                    nonlocal prev
                    new_value = value * 100.0
                    if int(new_value) > int(prev):
                        progress_bar.update(int(new_value - prev))
                    prev += new_value

            gdal.Translate(
                str(filepath),
                str(vrt_path),
                format=format,
                creationOptions=[f"{k}={v}" for k, v in creation_options.items()],
                callback=callback,
            )

    def add(self, other: int | float | "VRaster") -> "VRaster":
        """
        Perform addition on the VRaster

        Parameters
        ----------
        other
            A constant value or another VRaster to add.

        Returns
        -------
        A new VRaster
        """
        new_vraster = self.copy()
        new = new_vraster.last.copy()

        if isinstance(other, VRaster):
            if (message := self._check_compatibility(other)) is not None:
                raise AssertionError(message)

            for i, band in enumerate(new.raster_bands):
                if misc.nested_getattr(band, ["pixel_function", "name"]) == "scale":
                    band.sources.append(
                        SimpleSource(
                            source_filename=other.last,
                            source_band=i + 1,
                        )
                    )
                else:
                    new_band = VRTDerivedRasterBand.from_raster_band(
                        band=band, pixel_function=pixel_functions.SumPixelFunction()
                    )
                    new_band.sources = [
                        SimpleSource(
                            source_filename=new_vraster.last,
                            source_band=i + 1,
                        ),
                        SimpleSource(
                            source_filename=other.last,
                            source_band=i + 1,
                        ),
                    ]

                    new.raster_bands[i] = new_band
            name = "add_vraster"

        else:
            for i, band in enumerate(new.raster_bands):
                if misc.nested_getattr(band, ["pixel_function", "name"]) == "scale":
                    if band.offset is not None:
                        band.offset += other
                    else:
                        band.offset = other
                else:
                    new_band = VRTDerivedRasterBand.from_raster_band(band=band, pixel_function=ScalePixelFunction())
                    new_band.sources = [
                        SimpleSource(
                            source_filename=new_vraster.last,
                        )
                    ]
                    new_band.offset = other

                    new.raster_bands[i] = new_band
            name = "add_constant"

        new_vraster.steps.append(VRasterStep(new, name))
        return new_vraster

    def __add__(self, other: int | float | "VRaster") -> "VRaster":
        return self.add(other)

    def __radd__(self, other: int | float | "VRaster") -> "VRaster":
        return self.__add__(other)

    def multiply(self, other: int | float | "VRaster") -> "VRaster":
        """
        Perform multiplication on the VRaster

        Parameters
        ----------
        other
            A constant value or another VRaster to multiply.

        Returns
        -------
        A new VRaster
        """
        new_vraster = self.copy()

        new = new_vraster.last.copy()
        if isinstance(other, VRaster):
            if (message := self._check_compatibility(other)) is not None:
                raise AssertionError(message)

            for i, band in enumerate(new.raster_bands):
                if misc.nested_getattr(band, ["pixel_function", "name"]) == "mul":
                    band.sources.append(
                        SimpleSource(
                            source_filename=other.last,
                            source_band=i + 1,
                        )
                    )
                else:
                    new_band = VRTDerivedRasterBand.from_raster_band(
                        band=band, pixel_function=pixel_functions.MulPixelFunction()
                    )
                    new_band.sources = [
                        SimpleSource(
                            source_filename=new_vraster.last,
                            source_band=i + 1,
                        ),
                        SimpleSource(
                            source_filename=other.last,
                            source_band=i + 1,
                        ),
                    ]

                    new.raster_bands[i] = new_band

            # raise NotImplementedError("Not yet implemented for VRaster")
            name = "multiply_vraster"
        else:
            for i, band in enumerate(new.raster_bands):
                if misc.nested_getattr(band, ["pixel_function", "name"]) == "scale":
                    if band.scale is not None:
                        band.scale *= other
                    else:
                        band.scale = other
                    if band.offset is not None:
                        band.offset *= other
                else:
                    new_band = VRTDerivedRasterBand.from_raster_band(band=band, pixel_function=ScalePixelFunction())
                    new_band.sources = [
                        SimpleSource(
                            source_filename=new_vraster.last,
                        )
                    ]
                    new_band.scale = other

                    new.raster_bands[i] = new_band
            name = "multiply_constant"

        new_vraster.steps.append(VRasterStep(new, name))
        return new_vraster

    def __mul__(self, other: int | float | "VRaster") -> "VRaster":
        return self.multiply(other)

    def __rmul__(self, other: int | float | "VRaster") -> "VRaster":
        return self.__mul__(other)

    def __neg__(self) -> "VRaster":
        return self.multiply(-1)

    def warp(
        self,
        reference: "VRaster" | None = None,
        crs: CRS | int | str | None = None,
        res: tuple[float, float] | float | None = None,
        shape: tuple[int, int] | None = None,
        bounds: BoundingBox | list[float] | None = None,
        transform: Affine | None = None,
        resampling: Resampling | str = "bilinear",
        multithread: bool = False,
    ):
        """
        Warp the VRaster to new bounds, resolutions and/or coordinate systems.

        This wraps the functionality of gdal.Warp

        Parameters
        ----------
        reference
            Optional: A reference VRaster to get the CRS, transform and shape from.
            Note: It silently overrides the `shape`, `crs` and `transform` arguments.
            If only parts of the reference parameters should be used, supply them directly instead (e.g. VRaster.crs). 
        crs
            The target coordinate reference system (CRS).
            If an integer is given, it's parsed as an EPSG code (e.g. 4326 -> WGS84).
        res
            The target resolution in georeferenced units. If only one value is given, it is used for both axes.
        shape
            The target shape of the VRaster in pixels as (height, width).
        bounds
            The target corner bounds of the VRaster. If a list is given, it's parsed as [xmin, ymin, xmax, ymax]
        transform
            The target affine transform of the VRaster.
        resampling
            The target resampling algorithm, e.g. "bilinear" or "cubic_spline".
            See rio.warp.Resampling for all available algorithms.
        multithread
            Use multithreading for the warp operation.

        Returns
        -------
        A new VRaster
        """
        new_vraster = self.copy()

        warp_kwargs = {
            "dst_crs": crs,
            "dst_res": res,
            "dst_shape": shape,
            "dst_bounds": bounds,
            "dst_transform": transform,
            "resampling": resampling,
        }

        if reference is not None:
            for key, value in [
                ("dst_crs", reference.crs),
                ("dst_shape", reference.shape),
                ("dst_transform", reference.transform),
            ]:
                if warp_kwargs[key] is None:
                    warp_kwargs[key] = value

        with tempfile.TemporaryDirectory() as temp_dir:
            _, vrt_filepath = new_vraster.last.to_tempfiles(temp_dir)

            warped_path = vrt_filepath.with_stem("warped")
            vrt_warp(output_filepath=warped_path, input_filepath=vrt_filepath, **warp_kwargs)

            warped = load_vrt(warped_path)

            new_path = vrt_filepath.with_stem("new")
            build_vrt(new_path, warped_path)

            new = load_vrt(new_path)

        warped.source_dataset = new_vraster.last

        for band in new.raster_bands:
            band.sources = [SimpleSource(source_filename=warped, source_band=band.band)]

        new_vraster.steps.append(VRasterStep(warped, "warp"))
        new_vraster.steps.append(VRasterStep(new, "warp_wrapped"))

        return new_vraster

    def replace_nodata(self, value: int | float):
        """
        Replace all nodata pixels with the given value.

        Parameters
        ----------
        value
            The value to replace nodata with

        Returns
        -------
        A new VRaster
        """
        new_vraster = self.copy()
        new = new_vraster.last.copy()

        for i, band in enumerate(new.raster_bands):
            new_band = VRTDerivedRasterBand.from_raster_band(
                band=band, pixel_function=pixel_functions.ReplaceNodataPixelFunction(value=value)
            )
            new_band.sources = [SimpleSource(source_filename=new_vraster.last, source_band=i + 1)]
            new.raster_bands[i] = new_band

        new_vraster.steps.append(VRasterStep(new, "replace_nodata"))
        return new_vraster

    def inverse(self) -> "VRaster":
        """
        Invert the VRaster (1 / x)

        Returns
        -------
        A new VRaster.
        """
        new_vraster = self.copy()
        new = new_vraster.last.copy()
        for i, band in enumerate(new.raster_bands):
            new_band = VRTDerivedRasterBand.from_raster_band(
                band=band, pixel_function=pixel_functions.InvPixelFunction()
            )
            new_band.sources = [SimpleSource(source_filename=new_vraster.last, source_band=i + 1)]
            new.raster_bands[i] = new_band

        new_vraster.steps.append(VRasterStep(new, "inverse"))
        return new_vraster

    def divide(self, other: int | float | "VRaster") -> "VRaster":
        """
        Perform division on the VRaster

        Parameters
        ----------
        other
            A constant value or another VRaster to divide.

        Returns
        -------
        A new VRaster.
        """
        if isinstance(other, VRaster):
            new_vraster = self.copy()
            new = new_vraster.last.copy()
            if (message := self._check_compatibility(other)) is not None:
                raise AssertionError(message)

            for i, band in enumerate(new.raster_bands):
                new_band = VRTDerivedRasterBand.from_raster_band(
                    band=band, pixel_function=pixel_functions.DivPixelFunction()
                )
                new_band.sources = [
                    SimpleSource(
                        source_filename=new_vraster.last,
                        source_band=i + 1,
                    ),
                    SimpleSource(
                        source_filename=other.last.copy(),
                        source_band=i + 1,
                    ),
                ]

                new.raster_bands[i] = new_band

            new_vraster.steps.append(VRasterStep(new, "divide_vraster"))
            return new_vraster
        else:
            new = self.multiply(1 / other)
            new.steps[-1].name = "divide_constant"
        return new

    def __div__(self, other: int | float | "VRaster") -> "VRaster":
        return self.divide(other)

    def __rdiv__(self, other: int | float | "VRaster") -> "VRaster":
        return self.inverse().__rmul__(other)

    def __rtruediv__(self, other: int | float | "VRaster") -> "VRaster":
        return self.__rdiv__(other)

    def __truediv__(self, other: int | float | "VRaster") -> "VRaster":
        return self.__div__(other)

    def subtract(self, other: int | float | "VRaster") -> "VRaster":
        """
        Perform subtraction on the VRaster

        Parameters
        ----------
        other
            A constant value or another VRaster to subtract.

        Returns
        -------
        A new VRaster
        """
        if isinstance(other, VRaster):
            negative = other.multiply(-1)
            new = self.add(negative)
            new.steps[-1].name = "subtract_vraster"
        else:
            new = self.add(-other)
            new.steps[-1].name = "subtract_constant"
        return new

    def __sub__(self, other: int | float | "VRaster") -> "VRaster":
        return self.subtract(other)

    def __rsub__(self, other: int | float | "VRaster") -> "VRaster":
        return self.__neg__().__add__(other)

    @property
    def n_bands(self) -> int:
        return self.last.n_bands

    @property
    def crs(self) -> CRS:
        return self.last.crs

    @property
    def transform(self) -> Affine:
        return self.last.transform

    @property
    def bounds(self) -> BoundingBox:
        return self.last.bounds

    @property
    def res(self):
        return self.last.res

    def copy(self):
        return copy.deepcopy(self)

    @property
    def shape(self):
        return self.last.shape

    @property
    def last(self):
        return self.steps[-1].dataset

    @overload
    def sample(self, x_coord: float, y_coord: float, band: int, masked: bool) -> int | float:... 

    @overload
    def sample(self, x_coord: float, y_coord: float, band: list[int], masked: Literal[True]) -> np.ma.masked_array:... 

    @overload
    def sample(self, x_coord: float, y_coord: float, band: list[int], masked: Literal[False]) -> np.ndarray:... 

    @overload
    def sample(self, x_coord: Iterable[float], y_coord: Iterable[float], band: int | list[int], masked: Literal[False]) -> np.ndarray:... 

    @overload
    def sample(self, x_coord: Iterable[float], y_coord: Iterable[float], band: int | list[int], masked: Literal[True]) -> np.ma.masked_array:... 

    def sample(self, x_coord: float | Iterable[float], y_coord: float | Iterable[float], band: int | list[int] = 1, masked: bool = False) -> int | float | np.ndarray | np.ma.masked_array:
        """
        Sample values at the given georeferenced coordinates of a VRaster.

        Parameters
        ----------
        x_coord
            The x (easting/longitude) coordinate(s) to sample
        y_coord
            The x (northing/latitude) coordinate(s) to sample
        band
            The band(s) to sample from. Defaults to the first.
        masked
            Return a masked array with nodata values masked out.

        Returns
        -------
        If one coordinate and one band:
            One sampled value
        If multiple coordinates and/or multiple bands:
            An array of coordinates
        """
        if self.last.is_nested():
            with tempfile.TemporaryDirectory(prefix="variete") as temp_dir:
                return load_vrt(self.last.to_tempfiles(temp_dir=temp_dir)[1]).sample(
                    x_coord=x_coord, y_coord=y_coord, band=band, masked=masked
                )

        return self.steps[-1].dataset.sample(x_coord=x_coord, y_coord=y_coord, band=band, masked=masked)

    @overload
    def sample_rowcol(self, row: float, col: float, band: int, masked: bool) -> int | float: ...

    @overload
    def sample_rowcol(self, row: float, col: float, band: list[int], masked: Literal[True]) -> np.ma.masked_array: ...

    @overload
    def sample_rowcol(self, row: float, col: float, band: list[int], masked: Literal[False]) -> np.ndarray: ...

    @overload
    def sample_rowcol(self, row: Iterable[float], col: Iterable[float], band: int | list[int], masked: Literal[True]) -> np.ma.masked_array: ...

    @overload
    def sample_rowcol(self, row: Iterable[float], col: Iterable[float], band: int | list[int], masked: Literal[False]) -> np.ndarray: ...

    def sample_rowcol(self, row: float | Iterable[float], col: float | Iterable[float], band: int | list[int] = 1, masked: bool = False) -> int | float | np.ndarray | np.ma.masked_array:
        """
        Sample values at the given row(s) and column(s) of a VRaster.

        Parameters
        ----------
        row
            The row(s) to sample.
        y_coord
            The column(s) to sample.
        band
            The band(s) to sample from. Defaults to the first.
        masked
            Return a masked array with nodata values masked out.

        Returns
        -------
        If one coordinate and one band:
            One sampled value
        If multiple coordinates and/or multiple bands:
            An array of coordinates
        """
        x_coord, y_coord = rio.transform.xy(self.transform, row, col)
        return self.sample(x_coord, y_coord, band=band, masked=masked)


def load(filepath: str | Path, nodata_to_nan: bool = True) -> VRaster:
    """
    Load a VRaster from a file.

    Parameters
    ----------
    filepath
        The path to a GDAL-readable dataset.
    nodata_to_nan
        Whether to convert nodata values to np.nan on load

    Returns
    -------
    A new VRaster
    """
    vraster = VRaster.load_file(filepath)

    if nodata_to_nan:
        replace = False
        for band in vraster.last.raster_bands:
            if band.nodata is not None:
                replace = True

        if replace:
            vraster = vraster.replace_nodata(np.nan)

    return vraster
