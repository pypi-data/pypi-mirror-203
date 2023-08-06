from __future__ import annotations
import uuid

from lightningchart.ui_element import Axis
import lightningchart.charts


class Series:
    """Base class which all Series will inherit."""

    def __init__(self, chart: lightningchart.charts.Chart):
        self.chart = chart
        self.instance = chart.instance
        self.id = str(uuid.uuid4().hex)

    def dispose(self):
        """Permanently destroy the component.

        Returns:
            True
        """
        self.instance.send_command(self.id, 'dispose')
        return True

    def clear(self):
        """Clear all previously pushed data points from the series.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'clearSeries')
        return self

    def set_visible(self, visible: bool = True):
        """Set element visibility.

        Args:
            visible (bool): true when element should be visible and false when element should be hidden.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setVisible', {'visible': int(visible)})
        return self

    def set_highlight(self, highlight: bool = True):
        """
        Set state of component highlighting.
        Args:
            highlight: Boolean or number between 0 and 1, where 1 is fully highlighted.

        Returns:

        """
        self.instance.send_command(self.id, 'setHighlight', {'enabled': int(highlight)})
        return self


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class SeriesWithAddData(Series):

    def add_data(
            self,
            data: dict[str, int | float] | list[dict[str, int | float]],
            clear_previous: bool = False
    ):
        """Append a single datapoint or list of datapoints into the series.

        Args:
            data (dict[str, int | float] | list[dict[str, int | float]]): List of datapoints or a single datapoint.
            clear_previous (bool): If true, all previous datapoints are removed from the series.

        Returns:
            Reference to self.
        """
        self.instance.send_data(self.id, data, clear_previous)
        return self


class SeriesWithAddDataXY(Series):

    def add(
            self,
            x: list[int | float],
            y: list[int | float],
            clear_previous: bool = False
    ):
        """Add X and Y arrays to the series.

        Args:
            x (list[int | float]): List of x values
            y (list[int | float]): List of y values
            clear_previous (bool): If true, all previous datapoints are removed from the series.

        Returns:
            Reference to self.
        """
        if isinstance(x, int) or isinstance(x, float):
            x = [x]
        if isinstance(y, int) or isinstance(y, float):
            y = [y]
        if not isinstance(x, list):
            x = x.tolist()
        if not isinstance(y, list):
            y = y.tolist()

        self.instance.send_command(self.id, 'addDataXY', {
            'x': x,
            'y': y,
            'clear': clear_previous
        })
        return self


class SeriesWithAddDataXYZ(Series):

    def add(
            self,
            x: list[int | float],
            y: list[int | float],
            z: list[int | float],
            clear_previous: bool = False
    ):
        if not isinstance(x, list):
            x = x.tolist()
        if not isinstance(y, list):
            y = y.tolist()
        if not isinstance(z, list):
            z = z.tolist()

        self.instance.send_command(self.id, 'addDataXYZ', {
            'x': x,
            'y': y,
            'z': z,
            'clear': clear_previous
        })
        return self


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class SeriesWithDataCleaning(Series):
    """Prototype class for Series with data cleaning."""

    def enable_data_cleaning(self, enabled: bool):
        """Enable automatic data cleaning for series.

        Args:
            enabled (bool): If true, automatic data cleaning is performed.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setDataCleaning', {'enabled': enabled})
        return self


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class SeriesWithAddValues(Series):
    """Prototype class for Series with the method add_values()"""

    def add_values(
            self,
            y_values: list[list[int | float]] = None,
            intensity_values: list[list[int | float]] = None
    ):
        """Append values to the Surface Scrolling Grid Series.

        The series type can contain between 1 and 2 different data sets (Y values and Intensity values).
        This same method is used for managing both types of data;

        Args:
            y_values (list[list[int | float]]): a number matrix.
            intensity_values (list[list[int | float]]): a number matrix.

        Returns:
            Reference to self.
        """
        if y_values and not isinstance(y_values, list):
            y_values = y_values.tolist()

        if intensity_values and not isinstance(intensity_values, list):
            intensity_values = intensity_values.tolist()

        self.instance.send_command(self.id, 'addValues', {
            'yValues': y_values,
            'intensityValues': intensity_values
        })
        return self


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class SeriesWithInvalidateIntensity(Series):
    """Prototype class for Series with the method invalidate_intensity_values()"""

    def invalidate_intensity_values(
            self,
            data: list[list[int | float]],
            column_index: int = None,
            row_index: int = None
    ):
        """Invalidate range of surface intensity values starting from first column and row.

        Args:
            data (list[list[int | float]]): a number matrix.
            column_index (int): Index of first invalidated column.
            row_index (int): Index of first invalidated row.

        Returns:
            Reference to self.
        """
        if not isinstance(data, list):
            data = data.tolist()

        self.instance.send_command(self.id, 'invalidateIntensityValues', {
            'data': data,
            'column': column_index,
            'row': row_index
        })
        return self


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class SeriesWithAddIntensityValues(Series):
    """Prototype class for Series with the method add_intensity_values()"""

    def add_intensity_values(self, new_data_points: list[list[int | float]]):
        """Push a Matrix of intensity values into the Heatmap grid. Each value describes one cell in the grid.

        Args:
            new_data_points (list[list[int | float]]): a number matrix.

        Returns:
            Reference to self.
        """
        if not isinstance(new_data_points, list):
            new_data_points = new_data_points.tolist()

        self.instance.send_command(self.id, 'addIntensityValues', {'data': new_data_points})
        return self


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class SeriesWithInvalidateData(Series):
    """Prototype class for Series with the method invalidate_data()"""

    def invalidate_data(self, data: dict[str, int | float] | list[dict[str, int | float]]):
        """Method for invalidating Box data. Accepts an Array of BoxDataCentered objects.
        Properties that must be defined for each NEW Box:

        "xCenter", "yCenter", "zCenter" | coordinates of Box in Axis values.

        "xSize", "ySize", "zSize" | size of Box in Axis values.

        Args:
            data (dict[str, int | float] | list[dict[str, int | float]]): List of BoxDataCentered objects.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'invalidateData', {'data': data})
        return self


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class SeriesWithAddArray(Series):
    """Prototype class for Series with methods for adding individual data arrays."""

    def add_array_x(self, array: list[int | float]):
        """Append new data points into the series by only supplying X coordinates.

        Args:
            array (list[int | float]): List of numbers | Pandas DataFrame column | NumPy array

        Returns:
            Reference to self.
        """
        if not isinstance(array, list):
            array = array.tolist()

        # self.instance.send_num_array(self.id, 'addArrayX', array)
        self.instance.send_command(self.id, 'addArrayX', {'array': array})
        return self

    def add_array_y(self, array: list[int | float]):
        """Append new data points into the series by only supplying Y coordinates.

        Args:
            array (list[int | float]): List of numbers | Pandas DataFrame column | NumPy array

        Returns:
            Reference to self.
        """
        if not isinstance(array, list):
            array = array.tolist()

        # self.instance.send_num_array(self.id, 'addArrayY', array)
        self.instance.send_command(self.id, 'addArrayY', {'array': array})
        return self

    def add_arrays_xy(self, array_x: list[int | float], array_y: list[int | float]):
        """Append new data points into the series by supplying X and Y coordinates in two separated arrays.

        Args:
            array_x (list[int | float]): List of numbers | Pandas DataFrame column | NumPy array
            array_y (list[int | float]): List of numbers | Pandas DataFrame column | NumPy array

        Returns:
            Reference to self.
        """

        if not isinstance(array_x, list):
            array_x = array_x.tolist()
        if not isinstance(array_y, list):
            array_y = array_y.tolist()

        # self.instance.send_arrays_xy(self.id, array_x, array_y)
        self.instance.send_command(self.id, 'addArraysXY', {'arrayX': array_x, 'arrayY': array_y})
        return self


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class SeriesWithIndividualPoint(Series):
    """Prototype class for Series with individual point modification."""

    def set_individual_point_rotation_enabled(self, enabled: bool = True):
        """Enable or disable individual point rotation.
        When enabled, rotation for each point can be provided with the location of the point.

        Args:
            enabled (bool): Boolean state for individual point size enabled

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setIndividualPointRotationEnabled', {'enabled': enabled})
        return self

    def set_individual_point_size_enabled(self, enabled: bool = True):
        """Enable or disable individual point sizing.
        When enabled, size for each point can be provided with the location of the point.

        Args:
            enabled (bool): Boolean state for individual point size enabled

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setIndividualPointSizeEnabled', {'enabled': enabled})
        return self

    def set_individual_point_value_enabled(self, enabled: bool = True):
        """Enable or disable individual point value attributes.
        When enabled, each added data point can be associated with a numeric value attribute.

        Args:
            enabled (bool): Individual point values enabled or disabled.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setIndividualPointValueEnabled', {'enabled': enabled})
        return self


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class SeriesWith2DPoints(Series):
    """Prototype class for Series with 2D points."""

    def set_point_color(self, rgba: tuple[int, int, int] | tuple[int, int, int, int] = (255, 255, 255, 255)):
        """Set the color of all 2D datapoints within a series.

        Args:
            rgba (tuple[int, int, int] | tuple[int, int, int, int]): RGBA or RGB values between 0 and 255,
                e.g. (44, 138, 127) or (166, 20, 64, 128)

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setPointFillStyle', {'color': rgba})
        return self

    def set_point_size(self, size: int):
        """Set the size of all 2D datapoints within a series.

        Args:
            size (int): Size of a single datapoint in pixels.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setPoint2DSize', {'size': size})
        return self

    def set_point_rotation(self, degrees: int | float):
        """Set the rotation of all 2D datapoints within a series.

        Args:
            degrees (int | float): Rotation in degrees.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setPointRotation', {'angle': degrees})
        return self

    def set_paletted_point_fill_style(
            self,
            min_value: int | float,
            max_value: int | float,
            min_color_rgba: tuple[int, int, int] | tuple[int, int, int, int] = (0, 0, 0, 255),
            max_color_rgba: tuple[int, int, int] | tuple[int, int, int, int] = (255, 255, 255, 255),
            look_up_property: str = 'value'
    ):
        """Define a palette for dynamically looked up fill coloring in the series.

        Args:
            min_value (int | float): Minimum possible value for any given datapoint.
            max_value (int | float): Maximum possible value for any given datapoint.
            min_color_rgba (tuple[int, int, int] | tuple[int, int, int, int]): Color for the minimum value.
                RGBA or RGB values between 0 and 255, e.g. (44, 138, 127) or (166, 20, 64, 128)
            max_color_rgba (tuple[int, int, int] | tuple[int, int, int, int]): Color for the maximum value.
                RGBA or RGB values between 0 and 255, e.g. (44, 138, 127) or (166, 20, 64, 128)
            look_up_property (str): "value" | "x" | "y" | "z"

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setPalettedPointFillStyle', {
            'minValue': min_value,
            'maxValue': max_value,
            'minColor': min_color_rgba,
            'maxColor': max_color_rgba,
            'lookUpProperty': look_up_property
        })
        return self


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class SeriesWith3DPoints(Series):
    """Prototype class for Series with 3D points."""

    def set_point_color(self, rgba: tuple[int, int, int] | tuple[int, int, int, int] = (255, 255, 255, 255)):
        """Set the color of all 2D datapoints within a series.

        Args:
            rgba (tuple[int, int, int] | tuple[int, int, int, int]): RGBA or RGB values between 0 and 255,
                e.g. (44, 138, 127) or (166, 20, 64, 128)

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setPoint3DFillStyle', {'color': rgba})
        return self

    def set_point_size(self, size: int):
        """Set the size of all 3D datapoints within a series.

        Args:
            size (int): Size of a single datapoint.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setPoint3DSize', {'size': size})
        return self

    def set_point_shape(self, shape: str = 'sphere'):
        """Set the shape of all 3D datapoints within a series.

        Args:
            shape (str): "cube" | "sphere"

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setPoint3DShape', {'shape': shape})
        return self


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class SeriesWith2DLines(Series):
    """Prototype class for Series with 2D lines."""

    def set_line_color(self, rgba: tuple[int, int, int] | tuple[int, int, int, int] = (255, 255, 255, 255)):
        """Set the color of a 2D line series.

        Args:
            rgba (tuple[int, int, int] | tuple[int, int, int, int]): RGBA or RGB values between 0 and 255,
                e.g. (44, 138, 127) or (166, 20, 64, 128)

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setLineFillStyle', {'color': rgba})
        return self

    def set_line_thickness(self, thickness: int):
        """Set the thickness of a 2D line series.

        Args:
            thickness (int): Thickness of the line. Use -1 thickness to enable primitive line rendering.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setLineThickness', {'width': thickness})
        return self


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class SeriesWith3DLines(Series):
    """Prototype class for Series with 3D lines."""

    def set_line_color(self, rgba: tuple[int, int, int] | tuple[int, int, int, int] = (255, 255, 255, 255)):
        """Set the color of a 3D line series.

        Args:
            rgba (tuple[int, int, int] | tuple[int, int, int, int]): RGBA or RGB values between 0 and 255,
                e.g. (44, 138, 127) or (166, 20, 64, 128)

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setLineFillStyle', {'color': rgba})
        return self

    def set_line_thickness(self, thickness: int):
        """Set the thickness of a 3D line series.

        Args:
            thickness (int): Thickness of the line. Use -1 thickness to enable primitive line rendering.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setLineThickness', {'width': thickness})
        return self


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class SeriesWithHighLowFill(Series):
    """Prototype class for Series with High and Low value coloring."""

    def set_high_color(self, rgba: tuple[int, int, int] | tuple[int, int, int, int] = (255, 255, 255, 255)):
        """Set the color of high area of the series.

        Args:
            rgba (tuple[int, int, int] | tuple[int, int, int, int]): RGBA or RGB values between 0 and 255,
                e.g. (44, 138, 127) or (166, 20, 64, 128)

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setHighFillStyle', {'color': rgba})
        return self

    def set_low_color(self, rgba: tuple[int, int, int] | tuple[int, int, int, int] = (255, 255, 255, 255)):
        """Set the color of low are of the series.

        Args:
            rgba (tuple[int, int, int] | tuple[int, int, int, int]): RGBA or RGB values between 0 and 255,
                e.g. (44, 138, 127) or (166, 20, 64, 128)

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setLowFillStyle', {'color': rgba})
        return self


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class SeriesWithLUT(Series):
    """Prototype class for Series with lookup table coloring."""

    def set_paletted_fill_style(
            self,
            min_value: int | float,
            max_value: int | float,
            min_color_rgba: tuple[int, int, int] | tuple[int, int, int, int] = (0, 0, 0, 255),
            max_color_rgba: tuple[int, int, int] | tuple[int, int, int, int] = (255, 255, 255, 255),
            look_up_property: str = 'value'
    ):
        """Define a palette for dynamically looked up fill coloring in the series.

        Args:
            min_value (int | float): Minimum possible value for any given datapoint.
            max_value (int | float): Maximum possible value for any given datapoint.
            min_color_rgba (tuple[int, int, int] | tuple[int, int, int, int]): Color for the minimum value.
                RGBA or RGB values between 0 and 255, e.g. (44, 138, 127) or (166, 20, 64, 128)
            max_color_rgba (tuple[int, int, int] | tuple[int, int, int, int]): Color for the maximum value.
                RGBA or RGB values between 0 and 255, e.g. (44, 138, 127) or (166, 20, 64, 128)
            look_up_property (str): "value" | "x" | "y" | "z"

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setPalettedFillStyle', {
            'minValue': min_value,
            'maxValue': max_value,
            'minColor': min_color_rgba,
            'maxColor': max_color_rgba,
            'lookUpProperty': look_up_property
        })
        return self

    def set_solid_fill_style(
            self,
            color_rgba: tuple[int, int, int] | tuple[int, int, int, int] = (255, 255, 255, 255)
    ):
        """Set a solid color fill style for the series.

        Args:
            color_rgba (tuple[int, int, int] | tuple[int, int, int, int]): RGBA or RGB values between 0 and 255,
                e.g. (44, 138, 127) or (166, 20, 64, 128)

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setSolidFillStyle', {'color': color_rgba})
        return self

    def set_empty_fill_style(
            self,
            wireframe_color_rgba: tuple[int, int, int] | tuple[int, int, int, int] = (255, 255, 255, 255)
    ):
        """Singleton object which indicates that component should not have fill color.

        Args:
            wireframe_color_rgba (tuple[int, int, int] | tuple[int, int, int, int]): RGBA or RGB values between
                0 and 255, e.g. (44, 138, 127) or (166, 20, 64, 128)

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setEmptyFillStyle', {'color': wireframe_color_rgba})
        return self


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class SeriesWithWireframe(Series):
    """Prototype class for Series with wireframes."""

    def set_wireframe_style(
            self,
            style: str = 'empty',
            color_rgba: tuple[int, int, int] | tuple[int, int, int, int] = (255, 255, 255, 255)
    ):
        """Set the style of wireframe of the series.

        Args:
            style (str): "empty" | "solid"
            color_rgba (tuple[int, int, int] | tuple[int, int, int, int]): RGBA or RGB values between 0 and 255,
                e.g. (44, 138, 127) or (166, 20, 64, 128)

        Returns:
            Reference to self.
        """
        if style.lower() == 'empty':
            self.instance.send_command(self.id, 'setWireframeStyle', {'style': 'empty'})
        else:
            self.instance.send_command(self.id, 'setWireframeStyle', {
                'style': 'solid',
                'color': color_rgba
            })
        return self


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class SeriesWithInvalidateHeight(Series):
    """Prototype class for Series with height map."""

    def invalidate_height_map(
            self,
            data: list[list[int | float]],
            column_index: int = None,
            row_index: int = None
    ):
        """Invalidate range of surface height values starting from first column and row.
        These values correspond to coordinates along the Y axis.

        Args:
            data (list[list[int | float]]): a number matrix of height values.
            column_index (int): Index of the first column to be validated.
            row_index (int): Index of the first row to be validated.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'invalidateHeightMap', {
            'data': data,
            'column': column_index,
            'row': row_index
        })
        return self


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class SeriesWithIntensityInterpolation(Series):
    """Prototype class for Series with intensity interpolation."""

    def set_intensity_interpolation(self, interpolation: str = 'bilinear'):
        """Set surface intensity interpolation mode.

        Args:
            interpolation (str): "bilinear" | "disabled"

        Returns:
            Reference to self.
        """
        if interpolation.lower() == 'bilinear':
            self.instance.send_command(self.id, 'setIntensityInterpolation', {'interpolation': 'bilinear'})
        else:
            self.instance.send_command(self.id, 'setIntensityInterpolation', {'interpolation': 'disabled'})
        return self


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class SeriesWithPixelInterpolation(Series):
    """Prototype class for Series with pixel interpolation."""

    def set_pixel_interpolation(self, interpolation: str = 'bilinear'):
        """Set pixel interpolation mode.

         Args:
            interpolation (str): "bilinear" | "disabled"

        Returns:
            Reference to self.
        """
        if interpolation.lower() == 'bilinear':
            self.instance.send_command(self.id, 'setPixelInterpolationMode', {'interpolation': 'bilinear'})
        else:
            self.instance.send_command(self.id, 'setPixelInterpolationMode', {'interpolation': 'disabled'})
        return self


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class SeriesWithCull(Series):
    """Prototype class for Series with cull modes."""

    def set_cull_mode(self, mode: str = 'disabled'):
        """Set culling of the series.

        Args:
            mode (str): "disabled" | "cull-back" | "cull-front"

        Returns:
            Reference to self.
        """
        if mode.lower() == 'cull-back':
            self.instance.send_command(self.id, 'setCullMode', {'mode': 'cull-back'})
        elif mode.lower() == 'cull-front':
            self.instance.send_command(self.id, 'setCullMode', {'mode': 'cull-front'})
        else:
            self.instance.send_command(self.id, 'setCullMode', {'mode': 'disabled'})
        return self


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class SeriesWith3DShading(Series):
    """Prototype class for Series with 3D shading."""

    def set_color_shading_style(
            self,
            style: str = 'Phong',
            specular_reflection: float = 0.5,
            specular_color_rgba: tuple[int, int, int] | tuple[int, int, int, int] = (255, 255, 255, 255)
    ):
        """Set Color Shading Style for series.

        Args:
            style (str): "phong" | "simple"
            specular_reflection (float): Controls specular reflection strength. Value ranges from 0 to 1.
                Default is 0.1.
            specular_color_rgba (tuple[int, int, int] | tuple[int, int, int, int]): Specular highlight color.
                RGBA or RGB values between 0 and 255, e.g. (44, 138, 127) or (166, 20, 64, 128)

        Returns:
            Reference to self.
        """
        if style.lower().startswith('ph'):
            style = 'phong'
        else:
            style = 'simple'
        self.instance.send_command(self.id, 'setColorShadingStyle', {
            'style': style,
            'specularReflection': specular_reflection,
            'specularColor': specular_color_rgba
        })
        return self


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class Series2D(Series):
    """Prototype class for 2D series."""

    def set_cursor_enabled(self, enabled: bool = False):
        """Configure whether cursors should pick on this particular series or not.

        Args:
            enabled: boolean

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setCursorEnabled', {'enabled': enabled})
        return self


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class PointSeries2D(Series2D, SeriesWithAddData, SeriesWithAddDataXY, SeriesWith2DPoints, SeriesWithDataCleaning,
                    SeriesWithAddArray, SeriesWithIndividualPoint):
    """Series for visualizing 2D datapoints."""

    def __init__(
            self,
            chart: lightningchart.charts.Chart,
            data: dict[str, int | float] | list[dict[str, int | float]] = None,
            shape: str = None,
            x_axis: Axis = None,
            y_axis: Axis = None
    ):
        Series.__init__(self, chart)
        if str(shape).lower().startswith('tr'):
            shape = 2
        elif str(shape).lower().startswith('sq'):
            shape = 0
        else:
            shape = 1
        self.instance.send_command(self.id, 'pointSeries2D', {
            'chart': self.chart.id,
            'shape': shape,
            'xAxis': x_axis,
            'yAxis': y_axis
        })
        if data:
            self.add_data(data)

    def __str__(self):
        return 'PointSeries2D'


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class PointSeries3D(SeriesWithAddData, SeriesWithAddDataXYZ, SeriesWith3DPoints, SeriesWith3DShading):
    """Series for visualizing 3D datapoints."""

    def __init__(
            self,
            chart: lightningchart.charts.Chart,
            data: dict[str, int | float] | list[dict[str, int | float]] = None,
            render_2d: bool = False,
            individual_lookup_values_enabled: bool = False,
            individual_point_color_enabled: bool = False,
            individual_point_size_axis_enabled: bool = False,
            individual_point_size_enabled: bool = False
    ):
        Series.__init__(self, chart)
        self.instance.send_command(self.id, 'pointSeries3D', {
            'chart': self.chart.id,
            'individualLookupValuesEnabled': individual_lookup_values_enabled,
            'individualPointColorEnabled': individual_point_color_enabled,
            'individualPointSizeAxisEnabled': individual_point_size_axis_enabled,
            'individualPointSizeEnabled': individual_point_size_enabled,
            'type': render_2d
        })
        if data:
            self.add_data(data)

    def __str__(self):
        return 'PointSeries3D'


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class LineSeries2D(Series2D, SeriesWithAddData, SeriesWithAddDataXY, SeriesWith2DLines, SeriesWithDataCleaning,
                   SeriesWithAddArray):
    """Series for visualizing 2D lines."""

    def __init__(
            self,
            chart: lightningchart.charts.Chart,
            data: dict[str, int | float] | list[dict[str, int | float]] = None,
            data_pattern: str = None,
            x_axis: Axis = None,
            y_axis: Axis = None,
            individual_lookup_values_enabled: bool = False
    ):
        Series.__init__(self, chart)
        self.instance.send_command(self.id, 'lineSeries2D', {
            'chart': self.chart.id,
            'pattern': data_pattern,
            'xAxis': x_axis,
            'yAxis': y_axis,
            'individualLookupValuesEnabled': individual_lookup_values_enabled
        })
        if data:
            self.add_data(data)

    def __str__(self):
        return 'LineSeries2D'


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class LineSeries3D(SeriesWithAddData, SeriesWithAddDataXYZ, SeriesWith3DLines, SeriesWith3DShading):
    """Series for visualizing 3D lines."""

    def __init__(
            self,
            chart: lightningchart.charts.Chart,
            data: dict[str, int | float] | list[dict[str, int | float]] = None
    ):
        Series.__init__(self, chart)
        self.instance.send_command(self.id, 'lineSeries3D', {
            'chart': self.chart.id,
        })
        if data:
            self.add_data(data)

    def __str__(self):
        return 'LineSeries3D'


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class PointLineSeries2D(Series2D, SeriesWithAddData, SeriesWithAddDataXY, SeriesWith2DPoints, SeriesWith2DLines,
                        SeriesWithDataCleaning, SeriesWithAddArray, SeriesWithIndividualPoint):
    """Series for visualizing 2D lines with datapoints."""

    def __init__(
            self,
            chart: lightningchart.charts.Chart,
            data: dict[str, int | float] | list[dict[str, int | float]] = None,
            data_pattern: str = None,
            shape: str = None,
            x_axis: Axis = None,
            y_axis: Axis = None
    ):
        Series.__init__(self, chart)
        if str(shape).lower().startswith('tr'):
            shape = 2
        elif str(shape).lower().startswith('sq'):
            shape = 0
        else:
            shape = 1
        self.instance.send_command(self.id, 'pointLineSeries2D', {
            'chart': self.chart.id,
            'pattern': data_pattern,
            'shape': shape,
            'xAxis': x_axis,
            'yAxis': y_axis
        })
        if data:
            self.add_data(data)

    def __str__(self):
        return 'PointLineSeries2D'


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class PointLineSeries3D(SeriesWithAddData, SeriesWithAddDataXYZ, SeriesWith3DPoints, SeriesWith3DLines,
                        SeriesWith3DShading):
    """Series for visualizing 3D lines with datapoints."""

    def __init__(
            self,
            chart: lightningchart.charts.Chart,
            data: dict[str, int | float] | list[dict[str, int | float]] = None,
            render_2d: bool = False,
            individual_lookup_values_enabled: bool = False,
            individual_point_color_enabled: bool = False,
            individual_point_size_axis_enabled: bool = False,
            individual_point_size_enabled: bool = False
    ):
        Series.__init__(self, chart)
        self.instance.send_command(self.id, 'pointLineSeries3D', {
            'chart': self.chart.id,
            'individualLookupValuesEnabled': individual_lookup_values_enabled,
            'individualPointColorEnabled': individual_point_color_enabled,
            'individualPointSizeAxisEnabled': individual_point_size_axis_enabled,
            'individualPointSizeEnabled': individual_point_size_enabled,
            'type': render_2d
        })
        if data:
            self.add_data(data)

    def __str__(self):
        return 'PointLineSeries3D'


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class SplineSeries(Series2D, SeriesWithAddData, SeriesWithAddDataXY, SeriesWith2DLines, SeriesWith2DPoints,
                   SeriesWithAddArray, SeriesWithIndividualPoint):
    """Series for visualizing 2D splines."""

    def __init__(
            self,
            chart: lightningchart.charts.Chart,
            data: dict[str, int | float] | list[dict[str, int | float]] = None,
            data_pattern: str = None,
            shape: str = None,
            x_axis: Axis = None,
            y_axis: Axis = None
    ):
        Series.__init__(self, chart)
        if str(shape).lower().startswith('tr'):
            shape = 2
        elif str(shape).lower().startswith('sq'):
            shape = 0
        else:
            shape = 1
        self.instance.send_command(self.id, 'splineSeries', {
            'chart': self.chart.id,
            'pattern': data_pattern,
            'shape': shape,
            'xAxis': x_axis,
            'yAxis': y_axis
        })
        if data:
            self.add_data(data)

    def __str__(self):
        return 'SplineSeries'


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class OHLCSeries(Series2D, SeriesWithDataCleaning):
    def __init__(self, chart: lightningchart.charts.Chart, x_axis: Axis = None, y_axis: Axis = None):
        Series.__init__(self, chart)
        self.instance.send_command(self.id, 'OHLCSeries', {
            'chart': self.chart.id,
            'xAxis': x_axis,
            'yAxis': y_axis
        })

    def __str__(self):
        return 'OHLCSeries'

    def add(self, xohlc: tuple[int | float, int | float, int | float, int | float, int | float] | list[
        tuple[int | float, int | float, int | float, int | float, int | float]]):
        """Add OHLC segments to series. NOTE: Added segments must always have progressive X values!

        Args:
            xohlc: Tuple of X+OHLC values (X, Open, High, Low, Close) or array of such tuples

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'addOHLC', {
            'xohlc': xohlc
        })


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class BoxSeries2D(Series2D):
    def __init__(self, chart: lightningchart.charts.Chart, x_axis: Axis = None, y_axis: Axis = None):
        Series.__init__(self, chart)
        self.instance.send_command(self.id, 'boxSeries2D', {
            'chart': self.chart.id,
            'xAxis': x_axis,
            'yAxis': y_axis
        })

    def __str__(self):
        return 'BoxSeries2D'

    def add(
            self,
            start: int | float,
            end: int | float,
            median: int | float,
            lower_quartile: int | float,
            upper_quartile: int | float,
            lower_extreme: int | float,
            upper_extreme: int | float
    ):
        """Add new figure to the series.
        Args:
            start (int | float):
            end (int | float):
            median (int | float):
            lower_quartile (int | float):
            upper_quartile (int | float):
            lower_extreme (int | float):
            upper_extreme (int | float):

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'addBox2D', {
            'start': start,
            'end': end,
            'median': median,
            'lowerQuartile': lower_quartile,
            'upperQuartile': upper_quartile,
            'lowerExtreme': lower_extreme,
            'upperExtreme': upper_extreme
        })


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class BoxSeries3D(SeriesWithInvalidateData, SeriesWith3DShading):
    """Series for visualizing 3D boxes."""

    def __init__(self, chart: lightningchart.charts.Chart):
        Series.__init__(self, chart)
        self.instance.send_command(self.id, 'boxSeries3D', {'chart': self.chart.id})

    def __str__(self):
        return 'BoxSeries3D'


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class AreaSeries(Series2D, SeriesWithAddData, SeriesWithAddDataXY, SeriesWith2DLines, SeriesWithDataCleaning,
                 SeriesWithHighLowFill):
    """Series for visualizing 2D areas."""

    def __init__(
            self,
            chart: lightningchart.charts.Chart,
            data: dict[str, int | float] | list[dict[str, int | float]] = None,
            x_axis: Axis = None,
            y_axis: Axis = None
    ):
        Series.__init__(self, chart)
        self.instance.send_command(self.id, 'areaSeries', {
            'chart': self.chart.id,
            'xAxis': x_axis,
            'yAxis': y_axis
        })
        if data:
            self.add_data(data)

    def __str__(self):
        return 'AreaSeries'


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class AreaRangeSeries(Series2D, SeriesWithAddData, SeriesWithHighLowFill, SeriesWithDataCleaning):
    """Series for visualizing 2D areas with ranges."""

    def __init__(
            self,
            chart: lightningchart.charts.Chart,
            data: dict[str, int | float] | list[dict[str, int | float]] = None,
            x_axis: Axis = None,
            y_axis: Axis = None
    ):
        Series.__init__(self, chart)
        self.instance.send_command(self.id, 'areaRangeSeries', {
            'chart': self.chart.id,
            'xAxis': x_axis,
            'yAxis': y_axis
        })
        if data:
            self.add_data(data)

    def __str__(self):
        return 'AreaRangeSeries'


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class StepSeries(Series2D, SeriesWithAddData, SeriesWithAddDataXY, SeriesWith2DLines, SeriesWithAddArray,
                 SeriesWithIndividualPoint):
    """Series for visualizing 2D steps."""

    def __init__(
            self,
            chart: lightningchart.charts.Chart,
            data: dict[str, int | float] | list[dict[str, int | float]] = None,
            data_pattern: str = None,
            mode: int | float = None,
            shape: str = None,
            x_axis: Axis = None,
            y_axis: Axis = None
    ):
        Series.__init__(self, chart)
        self.instance.send_command(self.id, 'stepSeries', {
            'chart': self.chart.id,
            'pattern': data_pattern,
            'mode': mode,
            'shape': shape,
            'xAxis': x_axis,
            'yAxis': y_axis
        })
        if data:
            self.add_data(data)

    def __str__(self):
        return 'StepSeries'


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class HeatmapGridSeries(Series2D, SeriesWithLUT, SeriesWithInvalidateIntensity, SeriesWithIntensityInterpolation,
                        SeriesWithWireframe):
    """Series for visualizing 2D heatmap data in a grid."""

    def __init__(
            self,
            chart: lightningchart.charts.Chart,
            columns: int,
            rows: int,
            start: tuple[int, int] = (0, 0),
            end: tuple[int, int] = None,
            step: tuple[int, int] = (1, 1),
            data_order: str = 'columns',
            x_axis: Axis = None,
            y_axis: Axis = None
    ):
        Series.__init__(self, chart)
        self.instance.send_command(self.id, 'heatmapGridSeries', {
            'chart': self.chart.id,
            'columns': columns,
            'rows': rows,
            'start': start,
            'end': end,
            'step': step,
            'order': data_order,
            'xAxis': x_axis,
            'yAxis': y_axis
        })

    def __str__(self):
        return 'HeatmapGridSeries'


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class HeatmapScrollingGridSeries(Series2D, SeriesWithLUT, SeriesWithWireframe, SeriesWithPixelInterpolation,
                                 SeriesWithDataCleaning, SeriesWithAddIntensityValues):
    """Series for visualizing 2D heatmap data in a grid with automatic scrolling features."""

    def __init__(
            self,
            chart: lightningchart.charts.Chart,
            resolution: int,
            scroll_dimension: str = 'columns',
            start: tuple[int, int] = (0, 0),
            step: tuple[int, int] = (1, 1),
            x_axis: Axis = None,
            y_axis: Axis = None
    ):
        Series.__init__(self, chart)
        self.instance.send_command(self.id, 'heatmapScrollingGridSeries', {
            'chart': self.chart.id,
            'scroll': scroll_dimension,
            'resolution': resolution,
            'start': start,
            'step': step,
            'xAxis': x_axis,
            'yAxis': y_axis
        })

    def __str__(self):
        return 'HeatmapScrollingGridSeries'


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class SurfaceGridSeries(SeriesWithLUT, SeriesWithInvalidateIntensity, SeriesWithWireframe, SeriesWithInvalidateHeight,
                        SeriesWithIntensityInterpolation, SeriesWithCull, SeriesWith3DShading):
    """Series for visualizing 3D surface data in a grid."""

    def __init__(
            self,
            chart: lightningchart.charts.Chart,
            columns: int,
            rows: int,
            data_order: str = 'columns',
            start: tuple[int, int] = (0, 0),
            end: tuple[int, int] = None,
            step: tuple[int, int] = (1, 1)
    ):
        Series.__init__(self, chart)
        self.columns = columns
        self.rows = rows
        self.instance.send_command(self.id, 'surfaceGridSeries', {
            'chart': self.chart.id,
            'columns': columns,
            'rows': rows,
            'order': data_order,
            'start': start,
            'end': end,
            'step': step
        })

    def __str__(self):
        return 'SurfaceGridSeries'


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class SurfaceScrollingGridSeries(SeriesWithLUT, SeriesWithWireframe, SeriesWithIntensityInterpolation,
                                 SeriesWithCull, SeriesWithAddValues, SeriesWith3DShading):
    """Series for visualizing 3D surface data in a grid with automatic scrolling features."""

    def __init__(
            self,
            chart: lightningchart.charts.Chart,
            columns: int,
            rows: int,
            scroll_dimension: str = 'columns',
            start: tuple[int, int] = (0, 0),
            step: tuple[int, int] = (1, 1)
    ):
        Series.__init__(self, chart)
        self.instance.send_command(self.id, 'surfaceScrollingGridSeries', {
            'chart': self.chart.id,
            'columns': columns,
            'rows': rows,
            'scroll': scroll_dimension,
            'start': start,
            'step': step,
        })

    def __str__(self):
        return 'SurfaceScrollingGridSeries'


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class SpiderSeries:

    def __init__(self):
        pass

    def add_points(self):
        pass

    def set_auto_scrolling_enabled(self):
        pass

    def set_cursor_enabled(self):
        pass

    def set_effect(self):
        pass

    def set_fill_style(self):
        pass

    def set_highlight(self):
        pass

    def set_point_color(self):
        pass

    def set_point_rotation(self):
        pass

    def set_point_size(self):
        pass

    def set_stroke_style(self):
        pass


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class PolarSeries:

    def __init__(self):
        pass

    def dispose(self):
        pass

    def set_auto_scrolling_enabled(self):
        pass

    def set_cursor_enabled(self):
        pass

    def set_effect(self):
        pass

    def set_highlight(self):
        pass

    def set_visible(self):
        pass


class PolarPolygonSeries(PolarSeries):
    pass


class PolarAreaSeries(PolarSeries):
    pass


class PolarLineSeries(PolarSeries):
    pass


class PolarPointLineSeries(PolarSeries):
    pass


class PolarPointSeries(PolarSeries):
    pass
