from __future__ import annotations
import datetime
import uuid
from builtins import float

import lightningchart
from .instance import *
from .series import *
from .series import Series
from lightningchart.ui_element import *
from .ui_element import Axis


def axis_into_id(x_axis: Axis = None, y_axis: Axis = None):
    if x_axis:
        x_axis = x_axis.id
    if y_axis:
        y_axis = y_axis.id
    return x_axis, y_axis


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class Chart:
    def __init__(self, instance: Instance):
        self.id = str(uuid.uuid4().hex)
        self.instance = instance


class OpenChart(Chart):
    def open(self):
        """Open the rendering view.

        Returns:
            Reference to self.
        """
        self.instance.open()
        return self

    show = open


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class GeneralMethods(Chart):

    def save_to_file(
            self,
            file_name: str = None,
            image_format: str = 'image/png',
            image_quality: float = 0.92
    ):
        """Save the current rendering view as a screenshot.

        Args:
            file_name (str): Name of prompted download file as string. File extension shouldn't be included as it is
                automatically detected from 'type'-argument.
            image_format (str): A DOMString indicating the image format. The default format type is image/png.
            image_quality (float): A Number between 0 and 1 indicating the image quality to use for image formats that
                use lossy compression such as image/jpeg and image/webp. If this argument is anything else,
                the default value for image quality is used. The default value is 0.92.

        Returns:
            Reference to self.
        """
        if file_name is None:
            file_name = f'LightningChart Python {datetime.datetime.now().strftime("%Y-%m-%data %H.%M.%S")}'
        self.instance.send_command(self.id, 'saveToFile', {
            'fileName': file_name,
            'type': image_format,
            'encoderOptions': image_quality
        })
        return self

    def dispose(self) -> bool:
        """Permanently destroy the component.

        Returns:
            True
        """
        self.instance.send_command(self.id, 'dispose')
        return True

    def set_animations_enabled(self, enabled: bool = True):
        """Disable/Enable all animations of the Chart.

        Args:
            enabled (bool): Boolean value to enable or disable animations.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setAnimationsEnabled', {'enabled': enabled})
        return self

    def set_background_color(
            self,
            rgba: tuple[int, int, int] | tuple[int, int, int, int] = (255, 255, 255, 255)
    ):
        """Set the background color of the chart.

        Args:
            rgba (tuple[int, int, int] | tuple[int, int, int, int]): RGBA or RGB values between 0 and 255,
                e.g. (44, 138, 127) or (166, 20, 64, 128)

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setBackgroundFillStyle', {'color': rgba})
        return self

    def set_background_stroke(
            self,
            thickness: int | float,
            rgba: tuple[int, int, int] | tuple[int, int, int, int] = (255, 255, 255, 255)
    ):
        """Set chart background stroke style.

        Args:
            thickness (float): Thickness of the stroke.
            rgba (tuple[int, int, int] | tuple[int, int, int, int]): RGBA or RGB values between 0 and 255,
                e.g. (44, 138, 127) or (166, 20, 64, 128)

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setBackgroundStrokeStyle', {
            'thickness': thickness,
            'color': rgba
        })
        return self

    def add_legend(
            self,
            horizontal: bool = False,
            title: str = None,
            data: Chart | Series = None,
            x: int = None,
            y: int = None
    ) -> Legend:
        """Add legend box to the chart.

        Args:
            horizontal (bool): Whether the legend box is horizontally aligned or not.
            title (str): Title of the legend.
            data (Chart/Series): Reference either to Chart of Series class which the legend will display.
            x (int): X position in percentages (0-100).
            y (int): Y position in percentages (0-100).

        Returns:
            Reference to Legend Box class.
        """
        return Legend(chart=self, horizontal=horizontal, title=title, data=data, x=x, y=y)

    def add_textbox(
            self,
            text: str = None,
            x: int = None,
            y: int = None
    ):
        """Add text box to the chart.

        Args:
            text (str): Text of the text box.
            x (int): X position in percentages (0-100).
            y (int): Y position in percentages (0-100).

        Returns:
            Reference to Text Box class.
        """
        return TextBox(chart=self, text=text, x=x, y=y)


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class TitleMethods(Chart):

    def set_title(self, title: str):
        """Set text of Chart title.

        Args:
            title (str): Chart title as a string.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setTitle', {'title': title})
        return self

    def hide_title(self):
        """Hide title and remove padding around it.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'hideTitle')
        return self

    def set_title_color(self, rgba: tuple[int, int, int] | tuple[int, int, int, int] = (255, 255, 255, 255)):
        """Set color of Chart title.

        Args:
            rgba (tuple[int, int, int] | tuple[int, int, int, int]): RGBA or RGB values between 0 and 255,
                e.g. (44, 138, 127) or (166, 20, 64, 128)

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setTitleColor', {'color': rgba})
        return self

    def set_title_font(self, size: int | float, style: str):
        """Set font of Chart title.

        Args:
            size (int | float): Size of the font.
            style (Str): Style of the font, e.g. 'italic'

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setTitleFont', {'size': size, 'style': style})
        return self

    def set_title_margin(self, margin: int | float):
        """Specifies padding after chart title.

        Args:
            margin (int | float): Gap after the chart title in pixels.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setTitleMargin', {'margin': margin})
        return self

    def set_title_rotation(self, degrees: int | float):
        """Set rotation of Chart title.

        Args:
            degrees (int | float): Rotation in degrees.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setTitleRotation', {'value': degrees})
        return self

    def set_title_effect(self, enabled: bool = True):
        """Set theme effect enabled on component or disabled.

        Args:
            enabled (bool): Theme effect enabled.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setTitleEffect', {'enabled': enabled})
        return self


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class ChartWithXYAxis(Chart):

    def __init__(self):
        self.default_x_axis = DefaultAxis(self, 'x')
        self.default_y_axis = DefaultAxis(self, 'y')

    def get_default_x_axis(self) -> Axis:
        """Get the reference to the default x-axis of the chart.

        Returns:
            Reference to Axis class.
        """
        return self.default_x_axis

    def get_default_y_axis(self) -> Axis:
        """Get the reference to the default y-axis of the chart.

        Returns:
            Reference to Axis class.
        """
        return self.default_y_axis


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class ChartWithSeries(Chart):
    """Base class which ChartXY and Chart3D will inherit."""

    def __init__(self, instance: Instance):
        Chart.__init__(self, instance)
        self.series = []

    def clear(self):
        """Remove all series from the chart but not the chart itself.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'clearChart')
        return self

    def get_series(self) -> list[Series]:
        """Get references for all series in the chart.

        Returns:
            List of references to Series class.
        """
        return self.series

    def set_series_background_effect(self, enabled: bool = True):
        """Set theme effect enabled on component or disabled.

        Args:
            enabled (bool): Theme effect enabled.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setSeriesBackgroundEffect', {'enabled': enabled})
        return self

    def set_series_background_color(
            self,
            rgba: tuple[int, int, int] | tuple[int, int, int, int] = (255, 255, 255, 255)
    ):
        """Set chart series background color.

        Args:
            rgba (tuple[int, int, int] | tuple[int, int, int, int]): RGBA or RGB values between 0 and 255,
                e.g. (44, 138, 127) or (166, 20, 64, 128)

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setSeriesBackgroundFillStyle', {'color': rgba})
        return self

    def set_mouse_interactions(self, enabled: bool = True):
        """Set mouse interactions enabled or disabled.

        Args:
            enabled (bool): Specifies state of mouse interactions.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setMouseInteractions', {'bool': enabled})
        return self


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class ChartWithLUT(Chart):
    def set_lookup_table(
            self,
            min_value: int | float,
            max_value: int | float,
            min_color_rgba: tuple[int, int, int] | tuple[int, int, int, int] = (0, 0, 0, 255),
            max_color_rgba: tuple[int, int, int] | tuple[int, int, int, int] = (255, 255, 255, 255),
            interpolate: bool = True):
        """ Attach lookup table (LUT) to fill the slices with Colors based on value.

        Args:
            min_value (int | float): Minimum possible value for any given slice.
            max_value (int | float): Maximum possible value for any given slice.
            min_color_rgba (tuple[int, int, int] | tuple[int, int, int, int]): Color for the minimum value.
                RGBA or RGB values between 0 and 255, e.g. (44, 138, 127) or (166, 20, 64, 128)
            max_color_rgba (tuple[int, int, int] | tuple[int, int, int, int]): Color for the maximum value.
                RGBA or RGB values between 0 and 255, e.g. (44, 138, 127) or (166, 20, 64, 128)
            interpolate (bool): Whether color interpolation is used

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setLUT', {
            'minValue': min_value,
            'maxValue': max_value,
            'minColor': min_color_rgba,
            'maxColor': max_color_rgba,
            'interpolate': interpolate
        })
        return self


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class ChartWithLabelStyling(Chart):
    def set_label_color(self, rgba: tuple[int, int, int] | tuple[int, int, int, int] = (255, 255, 255, 255)):
        """Set the color of Slice Labels.

        Args:
            rgba (tuple[int, int, int] | tuple[int, int, int, int]): Color of the labels

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setLabelColor', {'color': rgba})
        return self

    def set_label_font(
            self,
            size: int | float = 20,
            family: str = 'Arial, Helvetica, sans-serif',
            weight: str = 'bold',
            style: str = 'italic',
    ):
        """Set font of Slice Labels.

        Args:
            size (int | float): CSS font size.
            family (str): CSS font family.
            weight (str): CSS font weight.
            style (str): CSS font style.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setLabelFont', {
            'size': size,
            'family': family,
            'weight': weight,
            'style': style
        })
        return self

    def set_label_effect(self, enabled: bool):
        """Set theme effect enabled on label or disabled. A theme can specify an Effect to add extra visual
        oomph to chart applications, like Glow effects around data or other components.

        Args:
            enabled (bool): Theme effect enabled.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setLabelEffect', {'enabled': enabled})
        return self

    def set_slice_effect(self, enabled: bool):
        """Set theme effect enabled on slice or disabled. A theme can specify an Effect to add extra visual
        oomph to chart applications, like Glow effects around data or other components.

        Args:
            enabled (bool): Theme effect enabled.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setSliceEffect', {'enabled': enabled})
        return self


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class ChartXY(OpenChart, GeneralMethods, TitleMethods, ChartWithXYAxis, ChartWithSeries):
    """Chart type for visualizing data between two dimensions, X and Y."""

    def __init__(
            self,
            theme: str = None,
            title: str = None
    ):
        """Create a XY Chart.

        Args:
            theme (str): "darkGold" | "light" | "flatDark" | "flatLight" | "lightNature" |
                "cyberSpace" | "turquoiseHexagon"
            title (str): A title for the chart.

        Returns:
            Reference to XY Chart class.
        """

        instance = lightningchart.Instance()
        ChartWithSeries.__init__(self, instance)
        ChartWithXYAxis.__init__(self)
        self.instance.send_command(self.id, 'chartXY', {'theme': theme})
        if title:
            self.instance.send_command(self.id, 'setTitle', {'title': title})

    def __str__(self):
        return 'XY Chart'

    def set_title_position(self, position: str = 'center-top') -> ChartXY:
        """ Set position of XY Chart title.

        Args:
            position (str): "right-top" | "left-top" | "right-bottom" | "left-bottom" | "center-top" |
                "center-bottom" | "series-center-top" | "series-right-top" | "series-left-top" |
                "series-center-bottom" | "series-right-bottom" | "series-left-bottom"

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setTitlePosition', {'position': position})
        return self

    def add_chart_marker(
            self,
            x_position: int | float = 0,
            y_position: int | float = 0
    ) -> ChartMarker:
        """Create a XY Chart Marker to be rendered as part of UI.

        Args:
            x_position (int | float): Position in the x-axis.
            y_position (int | float): Position in the y-axis.

        Returns:
            Reference to ChartMarker class.
        """
        return ChartMarker(self, x_position, y_position)

    def add_x_axis(
            self,
            opposite: bool,
            type: str = None,
            base: int = None
    ) -> Axis:
        """Add a new X Axis to the Chart.

        Args:
            opposite (bool): Specify Axis position in chart. Default is bottom for X Axes, and left for Y Axes.
                Setting to true will result in the opposite side (top for X Axes, right for Y Axes).
            type (str): "linear" | "linear-highPrecision" | "logarithmic"
            base (int): Specification of Logarithmic Base number (e.g. 10, 2, natural log). Defaults to 10 if omitted.
        Returns:
            Reference to Axis class.
        """
        return Axis(self, 'x', opposite, type, base)

    def add_y_axis(
            self,
            opposite: bool = None,
            type: str = None,
            base: int = None
    ) -> Axis:
        """Add a new Y Axis to the Chart.

        Args:
            opposite (bool): Specify Axis position in chart. Default is bottom for X Axes, and left for Y Axes.
                Setting to true will result in the opposite side (top for X Axes, right for Y Axes).
            type (str): "linear" | "linear-highPrecision" | "logarithmic"
            base (int): Specification of Logarithmic Base number (e.g. 10, 2, natural log). Defaults to 10 if omitted.
        Returns:
            Reference to Axis class.
        """
        return Axis(self, 'y', opposite, type, base)

    def set_cursor_mode(self, mode: str = "disabled") -> ChartXY:
        """Set chart AutoCursor behavior.

        Args:
            mode (str): "disabled" | "onHover" | "snapToClosest"

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setAutoCursorMode', {'mode': mode})
        return self

    def add_point_series(
            self,
            data: dict[str, int | float] | list[dict[str, int | float]] = None,
            shape: str = None,
            x_axis: Axis = None,
            y_axis: Axis = None
    ) -> PointSeries2D:
        """Method for adding a new PointSeries to the chart. This series type visualizes a list of Points
        (pair of X and Y coordinates), with configurable markers over each coordinate.

        Point Series 2D accepts data of form {x,y}

        Args:
            data (dict[str, int | float] | list[dict[str, int | float]]): List of XY datapoints.
            shape (str): "circle" | "square" | "triangle"
            x_axis (Axis): Optional non-default X Axis to attach series to.
            y_axis (Axis): Optional non-default Y Axis to attach series to.

        Returns:
            Reference to Point Series class.
        """
        x_axis, y_axis = axis_into_id(x_axis, y_axis)
        series = PointSeries2D(self, data, shape, x_axis, y_axis)
        self.series.append(series)
        return series

    def add_line_series(
            self,
            data: dict[str, int | float] | list[dict[str, int | float]] = None,
            data_pattern: str = None,
            x_axis: Axis = None,
            y_axis: Axis = None,
            individual_lookup_values_enabled: bool = False
    ) -> LineSeries2D:
        """Method for adding a new LineSeries to the chart. This series type visualizes a list of Points
        (pair of X and Y coordinates), with a continuous stroke.

        Line Series 2D accepts data of form {x,y}

        Args:
            data (dict[str, int | float] | list[dict[str, int | float]]): List of XY datapoints.
            data_pattern (str): "ProgressiveX" | "ProgressiveY" | "RegressiveX" | "RegressiveY"
            x_axis (Axis): Optional non-default X Axis to attach series to.
            y_axis (Axis): Optional non-default Y Axis to attach series to.
            individual_lookup_values_enabled (bool): Flag that can be used to enable data points value property on top
                of x and y. Disabled by default.

        Returns:
            Reference to Line Series class.
        """
        x_axis, y_axis = axis_into_id(x_axis, y_axis)
        series = LineSeries2D(
            self,
            data,
            data_pattern,
            x_axis,
            y_axis,
            individual_lookup_values_enabled
        )
        self.series.append(series)
        return series

    def add_point_line_series(
            self,
            data: dict[str, int | float] | list[dict[str, int | float]] = None,
            data_pattern: str = None,
            shape: str = None,
            x_axis: Axis = None,
            y_axis: Axis = None
    ) -> PointLineSeries2D:
        """Method for adding a new PointLineSeries to the chart. This series type visualizes a list of Points
        (pair of X and Y coordinates), with a continuous stroke and configurable markers over each coordinate.

        Point Line Series 2D accepts data of form {x,y}

        Args:
            data (dict[str, int | float] | list[dict[str, int | float]]): List of XY datapoints.
            data_pattern (str): "ProgressiveX" | "ProgressiveY" | "RegressiveX" | "RegressiveY"
            shape (str): "circle" | "square" | "triangle"
            x_axis (Axis): Optional non-default X Axis to attach series to.
            y_axis (Axis): Optional non-default Y Axis to attach series to.

        Returns:
            Reference to Point Line Series class.
        """
        x_axis, y_axis = axis_into_id(x_axis, y_axis)
        series = PointLineSeries2D(self, data, data_pattern, shape, x_axis, y_axis)
        self.series.append(series)
        return series

    def add_spline_series(
            self,
            data: dict[str, int | float] | list[dict[str, int | float]] = None,
            data_pattern: str = None,
            shape: str = None,
            x_axis: Axis = None,
            y_axis: Axis = None
    ) -> SplineSeries:
        """Method for adding a new SplineSeries to the chart. This series type visualizes a list of Points
        (pair of X and Y coordinates), with a smoothed curve stroke + point markers over each data point.

        Spline Series accepts data of form {x,y}

        Args:
            data (dict[str, int | float] | list[dict[str, int | float]]): List of XY datapoints.
            data_pattern (str): "ProgressiveX" | "ProgressiveY" | "RegressiveX" | "RegressiveY"
            shape (str): "Circle" | "Square" | "Triangle"
            x_axis (Axis): Optional non-default X Axis to attach series to.
            y_axis (Axis): Optional non-default Y Axis to attach series to.

        Returns:
            Reference to Spline Series class.
        """
        x_axis, y_axis = axis_into_id(x_axis, y_axis)
        series = SplineSeries(self, data, data_pattern, shape, x_axis, y_axis)
        self.series.append(series)
        return series

    def add_area_series(
            self,
            data: dict[str, int | float] | list[dict[str, int | float]] = None,
            x_axis: Axis = None,
            y_axis: Axis = None
    ) -> AreaSeries:
        """Method for adding a new AreaSeries to the chart. This series type is used for visualizing area between
        a static baseline and supplied curve data.

        Area Series accepts data of form {x,y}

        Args:
            data (dict[str, int | float] | list[dict[str, int | float]]): List of XY datapoints.
            x_axis (Axis): Optional non-default X Axis to attach series to.
            y_axis (Axis): Optional non-default Y Axis to attach series to.

        Returns:
            Reference to Area Series class.
        """
        x_axis, y_axis = axis_into_id(x_axis, y_axis)
        series = AreaSeries(self, data, x_axis, y_axis)
        self.series.append(series)
        return series

    def add_area_range_series(
            self,
            data: dict[str, int | float] | list[dict[str, int | float]] = None,
            x_axis: Axis = None,
            y_axis: Axis = None
    ) -> AreaRangeSeries:
        """Method for adding a new AreaRangeSeries to the chart.
        This series type is used for visualizing bands of data between two curves of data.

        Area Range Series accepts data of form {position, low, high}

        Args:
            data (dict[str, int | float] | list[dict[str, int | float]]): List of XY datapoints.
            x_axis (Axis): Optional non-default X Axis to attach series to.
            y_axis (Axis): Optional non-default Y Axis to attach series to.

        Returns:
            Reference to Area Range Series class.
        """
        x_axis, y_axis = axis_into_id(x_axis, y_axis)
        series = AreaRangeSeries(self, data, x_axis, y_axis)
        self.series.append(series)
        return series

    def add_step_series(
            self,
            data: dict[str, int | float] | list[dict[str, int | float]] = None,
            data_pattern: str = None,
            mode: str = None,
            point_shape: str = None,
            x_axis: Axis = None,
            y_axis: Axis = None
    ) -> StepSeries:
        """Method for adding a new StepSeries to the chart. This series type visualizes a list of Points
        (pair of X and Y coordinates), with a stepped stroke + point markers over each data point.

        Step Series accepts data of form {x,y}

        Args:
            data (dict[str, int | float] | list[dict[str, int | float]]): List of XY datapoints.
            data_pattern (str): "ProgressiveX" | "ProgressiveY" | "RegressiveX" | "RegressiveY"
            mode (str): "before": The y-value changes after the x-value. | "after": The y-value changes before the
                x-value. | "middle" : The y-value changes at the midpoint of each pair of adjacent x-values.
            point_shape (str): "Circle" | "Square" | "Triangle"
            x_axis (Axis): Optional non-default X Axis to attach series to.
            y_axis (Axis): Optional non-default Y Axis to attach series to.

        Returns:
            Reference to Step Series class.
        """
        x_axis, y_axis = axis_into_id(x_axis, y_axis)
        if str(mode).lower().startswith('mid'):
            mode = 0.5
        elif str(mode).lower().startswith('after'):
            mode = 1
        else:
            mode = 0
        series = StepSeries(self, data, data_pattern, mode, point_shape, x_axis, y_axis)
        self.series.append(series)
        return series

    def add_heatmap_grid_series(
            self,
            columns: int,
            rows: int,
            start: tuple[int, int] = (0, 0),
            step: tuple[int, int] = (1, 1),
            end: tuple[int, int] = None,
            data_order: str = 'columns',
            x_axis: Axis = None,
            y_axis: Axis = None
    ) -> HeatmapGridSeries:
        """Add a Series for visualizing a Heatmap Grid with a static column and grid count.

        Heatmap Grid Series accepts data in the form of two-dimensional matrix of correct size that includes
        integers or floats.

        Args:
            columns (int): Amount of columns (values on X Axis).
            rows (int):
            start (tuple[int,int]): Start coordinate of Heatmap on its X and Y Axes, e.g. (0,0)
            end (tuple[int,int]): End coordinate of Heatmap on its X and Y Axes. e.g. (4,4)
            step (tuple[int,int]): Step between each consecutive heatmap value on the X and Y Axes, e.g. (1,1)
            data_order (str): Specify how to interpret grid matrix values supplied by user. "columns" | "rows"
            x_axis (Axis): Optional non-default X Axis to attach series to.
            y_axis (Axis): Optional non-default Y Axis to attach series to.

        Returns:
            Reference to Heatmap Grid Series class.
        """
        x_axis, y_axis = axis_into_id(x_axis, y_axis)
        series = HeatmapGridSeries(
            self,
            columns,
            rows,
            start,
            end,
            step,
            data_order,
            x_axis,
            y_axis
        )
        self.series.append(series)
        return series

    def add_heatmap_scrolling_grid_series(
            self,
            resolution: int,
            scroll_dimension: str = 'columns',
            start: tuple[int, int] = (0, 0),
            step: tuple[int, int] = (1, 1),
            x_axis: Axis = None,
            y_axis: Axis = None
    ) -> HeatmapScrollingGridSeries:
        """Add a Series for visualizing a Heatmap Grid, with API for pushing data in a scrolling manner
        (append new data on top of existing data).

        Heatmap Scrolling Grid Series accepts data in the form of two-dimensional matrix of correct size that includes
        integers or floats.

        Args:
            resolution (int): Static amount of columns (cells on X Axis) OR rows (cells on Y Axis).
            scroll_dimension (str): Select scrolling dimension, as well as how to interpret grid matrix values supplied
                by user. "columns" | "rows"
            start (tuple[int,int]): Start coordinate of Heatmap on its X and Y Axes, e.g. (0,0)
            step (tuple[int,int]): Step between each consecutive heatmap value on the X and Y Axes, e.g. (1,1)
            x_axis (Axis): Optional non-default X Axis to attach series to.
            y_axis (Axis): Optional non-default Y Axis to attach series to.

        Returns:
            Reference to Heatmap Scrolling Grid Series class.
        """
        x_axis, y_axis = axis_into_id(x_axis, y_axis)
        series = HeatmapScrollingGridSeries(
            self,
            resolution,
            scroll_dimension,
            start,
            step,
            x_axis,
            y_axis
        )
        self.series.append(series)
        return series

    def add_box_series(self, x_axis: Axis = None, y_axis: Axis = None) -> BoxSeries2D:
        """

        Args:
            x_axis (Axis): Optional non-default X Axis to attach series to.
            y_axis (Axis): Optional non-default Y Axis to attach series to.

        Returns:
            Reference to Box Series class.
        """
        x_axis, y_axis = axis_into_id(x_axis, y_axis)
        series = BoxSeries2D(self, x_axis, y_axis)
        self.series.append(series)
        return series

    def add_ohlc_series(self, x_axis: Axis = None, y_axis: Axis = None) -> OHLCSeries:
        """

        Args:
            x_axis (Axis): Optional non-default X Axis to attach series to.
            y_axis (Axis): Optional non-default Y Axis to attach series to.

        Returns:
            Reference to OHLC Series class.
        """
        x_axis, y_axis = axis_into_id(x_axis, y_axis)
        series = OHLCSeries(self, x_axis, y_axis)
        self.series.append(series)
        return series


class ChartXYDashboard(ChartXY):
    """Class for ChartXY contained in Dashboard."""

    def __init__(
            self,
            instance: Instance,
            dashboard_id: str,
            column: int,
            row: int,
            colspan: int,
            rowspan: int,
            title: str = None
    ):
        ChartWithSeries.__init__(self, instance)
        ChartWithXYAxis.__init__(self)
        self.instance.send_command(self.id, 'createChartXY', {
            'db': dashboard_id,
            'column': column,
            'row': row,
            'colspan': colspan,
            'rowspan': rowspan
        })
        if title:
            self.instance.send_command(self.id, 'setTitle', {'title': title})

    def __str__(self):
        return 'XY Chart'


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class LineChart(ChartXY):

    def __init__(self, x=None, y=None, theme=None, title=None):
        instance = lightningchart.Instance()
        ChartWithSeries.__init__(self, instance)
        ChartWithXYAxis.__init__(self)
        self.series = str(uuid.uuid4().hex)
        self.instance.send_command(self.id, 'chartXY', {'theme': theme})
        if title:
            self.instance.send_command(self.id, 'setTitle', {'title': title})
        self.instance.send_command(self.series, 'lineSeries2D', {
            'chart': self.id,
            'pattern': None,
            'xAxis': None,
            'yAxis': None,
            'individualLookupValuesEnabled': None
        })
        self.instance.send_command(self.series, 'setLineThickness', {'width': 10})
        if x or y:
            self.add(x, y)

    def add(self, x=None, y=None):
        """Add X and Y arrays to the series.

        Args:
            x (list[int | float]): List of x values
            y (list[int | float]): List of y values

        Returns:
            Reference to self.
        """
        if isinstance(x, int) or isinstance(x, float):
            x = [x]
        if isinstance(y, int) or isinstance(y, float):
            y = [y]

        if x and y:
            self.instance.send_command(self.series, 'addArraysXY', {'arrayX': x, 'arrayY': y})
        elif y:
            self.instance.send_command(self.series, 'addArrayY', {'array': y})
        elif x:
            self.instance.send_command(self.series, 'addArrayX', {'array': x})
        return self

    def add_data(
            self,
            data: dict[str, int | float] | list[dict[str, int | float]],
            clear_previous: bool = False
    ):
        """Append a single datapoint or list of datapoints into the chart.

        Args:
            data (dict[str, int | float] | list[dict[str, int | float]]): List of datapoints or a single datapoint.
            clear_previous (bool): If true, all previous datapoints are removed from the series.

        Returns:
            Reference to self.
        """
        self.instance.send_data(self.series, data, clear_previous)
        return self


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class ScatterPlot(ChartXY):

    def __init__(self, x=None, y=None, theme=None, title=None):
        instance = lightningchart.Instance()
        ChartWithSeries.__init__(self, instance)
        ChartWithXYAxis.__init__(self)
        self.series = str(uuid.uuid4().hex)
        self.instance.send_command(self.id, 'chartXY', {'theme': theme})
        if title:
            self.instance.send_command(self.id, 'setTitle', {'title': title})
        self.instance.send_command(self.series, 'pointSeries2D', {
            'chart': self.id,
            'shape': 1,
            'xAxis': None,
            'yAxis': None
        })
        self.instance.send_command(self.series, 'setPoint2DSize', {'size': 10})
        if x or y:
            self.add(x, y)

    def add(self, x=None, y=None):
        """Add X and Y arrays to the series.

        Args:
            x (list[int | float]): List of x values
            y (list[int | float]): List of y values

        Returns:
            Reference to self.
        """
        if isinstance(x, int) or isinstance(x, float):
            x = [x]
        if isinstance(y, int) or isinstance(y, float):
            y = [y]

        if x and y:
            self.instance.send_command(self.series, 'addArraysXY', {'arrayX': x, 'arrayY': y})
        elif y:
            self.instance.send_command(self.series, 'addArrayY', {'array': y})
        elif x:
            self.instance.send_command(self.series, 'addArrayX', {'array': x})
        return self

    def add_data(
            self,
            data: dict[str, int | float] | list[dict[str, int | float]],
            clear_previous: bool = False
    ):
        """Append a single datapoint or list of datapoints into the chart.

        Args:
            data (dict[str, int | float] | list[dict[str, int | float]]): List of datapoints or a single datapoint.
            clear_previous (bool): If true, all previous datapoints are removed from the series.

        Returns:
            Reference to self.
        """
        self.instance.send_data(self.series, data, clear_previous)
        return self


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class Chart3D(OpenChart, GeneralMethods, TitleMethods, ChartWithXYAxis, ChartWithSeries):
    """Chart for visualizing data in a 3-dimensional scene, with camera and light source(s)."""

    def __init__(
            self,
            theme: str = None,
            title: str = None
    ):
        """Create a 3D Chart.

        Args:
            theme (str): "darkGold" | "light" | "flatDark" | "flatLight" | "lightNature" |
                "cyberSpace" | "turquoiseHexagon"
            title (str): A title for the chart.

        Returns:
            Reference to 3D Chart class.
        """
        instance = lightningchart.Instance()
        ChartWithSeries.__init__(self, instance)
        ChartWithXYAxis.__init__(self)
        self.default_z_axis = DefaultAxis(self, 'z')
        self.instance.send_command(self.id, 'chart3D', {'theme': theme})
        if title:
            self.instance.send_command(self.id, 'setTitle', {'title': title})

    def __str__(self):
        return '3D Chart'

    def get_default_z_axis(self) -> Axis:
        """Get the reference to the default x-axis of the chart.

        Returns:
            Reference to Axis class.
        """
        return self.default_y_axis

    def set_animation_zoom(self, enabled: bool = True) -> Chart3D:
        """Set Chart3D zoom animation enabled.
        When enabled, zooming with mouse wheel or trackpad will include a short animation. This is enabled by default.

        Args:
            enabled (bool): Boolean.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setAnimationZoom', {'enabled': enabled})
        return self

    def set_bounding_box(self, x: int | float = 1.0, y: int | float = 1.0, z: int | float = 1.0) -> Chart3D:
        """Set the dimensions of the Scenes bounding box. The bounding box is a visual reference that all the data of
        the Chart is depicted inside. The Axes of the 3D chart are always positioned along the sides of the bounding
        box.

        Args:
            x (int | float): Relative ratio of x dimension.
            y (int | float): Relative ratio of y dimension.
            z (int | float): Relative ratio of z dimension.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setBoundingBox', {'x': x, 'y': y, 'z': z})
        return self

    def set_bounding_box_stroke_style(
            self,
            thickness: int | float,
            color_rgba: tuple[int, int, int] | tuple[int, int, int, int] = (255, 255, 255, 255)
    ) -> Chart3D:
        """Set style of 3D bounding box.

        Args:
            thickness (int | float): Thickness of the bounding box.
            color_rgba (tuple[int, int, int] | tuple[int, int, int, int]): Color of the bounding box.
                RGBA or RGB values between 0 and 255, e.g. (44, 138, 127) or (166, 20, 64, 128)

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setBoundingBoxStrokeStyle', {
            'thickness': thickness,
            'color': color_rgba
        })
        return self

    def add_point_series(
            self,
            data: dict[str, int | float] | list[dict[str, int | float]] = None,
            render_2d: bool = False,
            individual_lookup_values_enabled: bool = False,
            individual_point_color_enabled: bool = False,
            individual_point_size_axis_enabled: bool = False,
            individual_point_size_enabled: bool = False
    ) -> PointSeries3D:
        """Method for adding a new PointSeries3D to the chart. This series type for visualizing a collection of
        { x, y, z } coordinates by different markers.

        Point Series 3D accepts data of form {x,y,z}

        Args:
            data (dict[str, int | float] | list[dict[str, int | float]]): List of XYZ datapoints.
            render_2d (bool): Defines the rendering type of Point Series. When true, points are rendered by 2D markers.
            individual_lookup_values_enabled (bool): Flag that can be used to enable data points value property on
                top of x, y and z. By default, this is disabled.
            individual_point_color_enabled (bool): Flag that can be used to enable data points color property on top of
                x, y and z. By default, this is disabled.
            individual_point_size_axis_enabled (bool): Flag that can be used to enable data points 'sizeAxisX',
                'sizeAxisY' and 'sizeAxisZ' properties on top of x, y and z. By default, this is disabled.
            individual_point_size_enabled (bool): Flag that can be used to enable data points size property on top of
                x, y and z. By default, this is disabled.

        Returns:
            Reference to Point Series class.
        """
        series = PointSeries3D(
            self,
            data,
            render_2d,
            individual_lookup_values_enabled,
            individual_point_color_enabled,
            individual_point_size_axis_enabled,
            individual_point_size_enabled
        )
        self.series.append(series)
        return series

    def add_line_series(
            self,
            data: dict[str, int | float] | list[dict[str, int | float]] = None
    ) -> LineSeries3D:
        """Method for adding a new LineSeries3D to the chart. This Series type for visualizing a collection of
        { x, y, z } coordinates by a continuous line stroke.

        Line Series 3D accepts data of form {x,y,z}

        Args:
            data (dict[str, int | float] | list[dict[str, int | float]]): List of XYZ datapoints.

        Returns:
            Reference to Line Series class.
        """
        series = LineSeries3D(self, data)
        self.series.append(series)
        return series

    def add_point_line_series(
            self,
            data: dict[str, int | float] | list[dict[str, int | float]] = None,
            render_2d: bool = False,
            individual_lookup_values_enabled: bool = False,
            individual_point_color_enabled: bool = False,
            individual_point_size_axis_enabled: bool = False,
            individual_point_size_enabled: bool = False
    ) -> PointLineSeries3D:
        """Method for adding a new PointLineSeries3D to the chart. This Series type for visualizing a collection of
        { x, y, z } coordinates by a continuous line stroke and markers.

        Point Line Series 3D accepts data of form {x,y,z}

        Args:
            data (dict[str, int | float] | list[dict[str, int | float]]): List of XYZ datapoints.
            render_2d (bool): Defines the rendering type of Point Series. When true, points are rendered by 2D markers.
            individual_lookup_values_enabled (bool): Flag that can be used to enable data points value property on
                top of x, y and z. By default, this is disabled.
            individual_point_color_enabled (bool): Flag that can be used to enable data points color property on top of
                x, y and z. By default, this is disabled.
            individual_point_size_axis_enabled (bool): Flag that can be used to enable data points 'sizeAxisX',
                'sizeAxisY' and 'sizeAxisZ' properties on top of x, y and z. By default, this is disabled.
            individual_point_size_enabled (bool): Flag that can be used to enable data points size property on top of
                x, y and z. By default, this is disabled.

        Returns:
            Reference to Point Line Series class.
        """
        series = PointLineSeries3D(
            self,
            data,
            render_2d,
            individual_lookup_values_enabled,
            individual_point_color_enabled,
            individual_point_size_axis_enabled,
            individual_point_size_enabled
        )
        self.series.append(series)
        return series

    def add_box_series(self) -> BoxSeries3D:
        """Create Series for visualization of large sets of individually configurable 3D Boxes.

        Box Series 3D accepts data of form { xCenter, yCenter, zCenter, xSize, ySize, zSize}

        Returns:
            Reference to Box Series class.
        """
        series = BoxSeries3D(self)
        self.series.append(series)
        return series

    def add_surface_grid_series(
            self,
            columns: int,
            rows: int,
            data_order: str = 'columns',
            start: tuple[int, int] = (0, 0),
            step: tuple[int, int] = (1, 1),
            end: tuple[int, int] = None
    ) -> SurfaceGridSeries:
        """Add a Series for visualizing a Surface Grid with a static column and grid count.

        Surface Grid Series accepts data in the form of two-dimensional matrix of correct size that includes
        integers or floats.

        Args:
            columns (int): Amount of cells along X axis.
            rows (int): Amount of cells along Y axis.
            data_order (str): "columns" | "rows"
            start (tuple[int,int]): Specifies location of first cell on X and Z axes. Optional, defaults to (0,0)
            end (tuple[int,int]): Specifies location of last cell on X and Z axes, e.g (4,4)
            step (tuple[int,int]): Specifies step between cells on X and Z axes. Optional, defaults to (1,1),
                unless end is specified.

        Returns:
            Reference to Surface Grid Series class.
        """
        series = SurfaceGridSeries(self, columns, rows, data_order, start, end, step)
        self.series.append(series)
        return series

    def add_surface_scrolling_grid_series(
            self,
            columns: int,
            rows: int,
            scroll_dimension: str = 'columns',
            start: tuple[int, int] = (0, 0),
            step: tuple[int, int] = (1, 1)
    ) -> SurfaceScrollingGridSeries:
        """Add a Series for visualizing a Surface Grid with API for pushing data in a scrolling manner
        (append new data on top of existing data).

        Surface Scrolling Grid Series accepts data in the form of two-dimensional matrix of correct size that includes
        integers or floats.

        Args:
            columns (int): Amount of cells along X axis.
            rows (int): Amount of cells along Y axis.
            scroll_dimension (str): Select scrolling dimension,
                as well as how to interpret grid matrix values supplied by user. "columns" | "rows"
            start (tuple[int,int]): Specifies location of first cell on X and Z axes. Optional, defaults to (0,0)
            step (tuple[int,int]): Specifies step between cells on X and Z axes. Optional, defaults to (1,1)

        Returns:
            Reference to Surface Scrolling Grid Series class.
        """
        series = SurfaceScrollingGridSeries(self, columns, rows, scroll_dimension, start, step)
        self.series.append(series)
        return series


class Chart3DDashboard(Chart3D):
    """Class for Chart3D contained in Dashboard."""

    def __init__(
            self,
            instance: Instance,
            dashboard_id: str,
            column: int,
            row: int,
            colspan: int,
            rowspan: int,
            title: str = None
    ):
        ChartWithSeries.__init__(self, instance)
        ChartWithXYAxis.__init__(self)
        self.instance.send_command(self.id, 'createChart3D', {
            'db': dashboard_id,
            'column': column,
            'row': row,
            'colspan': colspan,
            'rowspan': rowspan
        })
        if title:
            self.instance.send_command(self.id, 'setTitle', {'title': title})

    def __str__(self):
        return '3D Chart'


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class Dashboard(OpenChart, GeneralMethods):
    """Dashboard is a tool for rendering multiple charts in the same view."""

    def __init__(
            self,
            columns: int,
            rows: int,
            theme: str = None
    ):
        """Create a dashboard, i.e., a tool for rendering multiple charts in the same view.

        Args:
            columns (int): The amount of columns in the dashboard.
            rows (int): The amount of rows in the dashboard.
            theme (str): "darkGold" | "light" | "flatDark" | "flatLight" | "lightNature" |
                "cyberSpace" | "turquoiseHexagon"

        Returns:
            Reference to Dashboard class.
        """
        instance = lightningchart.Instance()
        Chart.__init__(self, instance)
        self.charts = []
        self.columns = columns
        self.rows = rows
        instance.send_command(self.id, 'dashboard', {
            'columns': columns,
            'rows': rows,
            'theme': theme
        })

    def __str__(self):
        return 'Dashboard'

    def ChartXY(
            self,
            column_index: int,
            row_index: int,
            column_span: int = 1,
            row_span: int = 1,
            title: str = None
    ) -> ChartXY:
        """Constructor for XY Chart within a dashboard.

        Args:
            column_index (int): Column index of the dashboard where the chart will be located.
            row_index (int): Row index of the dashboard where the chart will be located.
            column_span (int): How many columns the chart will take (X width). Default = 1.
            row_span (int): How many rows the chart will take (Y height). Default = 1.
            title (str): The title of the chart.

        Returns:
            Reference to XY Chart class.
        """
        return ChartXYDashboard(
            instance=self.instance,
            dashboard_id=self.id,
            column=column_index,
            row=row_index,
            colspan=column_span,
            rowspan=row_span,
            title=title
        )

    def Chart3D(
            self,
            column_index: int,
            row_index: int,
            column_span: int = 1,
            row_span: int = 1,
            title: str = None
    ) -> Chart3D:
        """Constructor for 3D chart within a dashboard.

        Args:
            column_index (int): Column index of the dashboard where the chart will be located.
            row_index (int): Row index of the dashboard where the chart will be located.
            column_span (int): How many columns the chart will take (X width). Default = 1.
            row_span (int): How many rows the chart will take (Y height). Default = 1.
            title (str): The title of the chart.

        Returns:
            Reference to 3D Chart class.
        """
        return Chart3DDashboard(
            instance=self.instance,
            dashboard_id=self.id,
            column=column_index,
            row=row_index,
            colspan=column_span,
            rowspan=row_span,
            title=title
        )

    def ZoomBandChart(
            self,
            chart: ChartXY,
            column_index: int,
            row_index: int,
            column_span: int = 1,
            row_span: int = 1,
            axis: Axis | str = 'x'
    ) -> ZoomBandChart:
        """Constructor for Zoom Band Chart within a dashboard.

        Args:
            chart (ChartXY): Reference to XY Chart which the Zoom Band Chart will use.
            column_index (int): Column index of the dashboard where the chart will be located.
            row_index (int): Row index of the dashboard where the chart will be located.
            column_span (int): How many columns the chart will take (X width). Default = 1.
            row_span (int): How many rows the chart will take (Y height). Default = 1.
            axis (Axis | str): "x" or "y" for the default axes, Axis class reference for custom axis.
                This is the axis that the  ZoomBandChart is attached to.

        Returns:
            Reference to Zoom Band Chart class.
        """
        if not isinstance(axis, str):
            axis = axis.id

        return ZoomBandChart(
            instance=self.instance,
            dashboard_id=self.id,
            chart_id=chart.id,
            column_index=column_index,
            column_span=column_span,
            row_index=row_index,
            row_span=row_span,
            axis=axis
        )

    def PieChart(
            self,
            column_index: int,
            row_index: int,
            column_span: int = 1,
            row_span: int = 1,
            title: str = None
    ) -> PieChart:
        return PieChartDashboard(
            instance=self.instance,
            dashboard_id=self.id,
            column=column_index,
            row=row_index,
            colspan=column_span,
            rowspan=row_span
        )

    def GaugeChart(
            self,
            column_index: int,
            row_index: int,
            column_span: int = 1,
            row_span: int = 1,
            title: str = None
    ) -> GaugeChart:
        return GaugeChartDashboard(
            instance=self.instance,
            dashboard_id=self.id,
            column=column_index,
            row=row_index,
            colspan=column_span,
            rowspan=row_span
        )

    def FunnelChart(
            self,
            column_index: int,
            row_index: int,
            column_span: int = 1,
            row_span: int = 1
    ) -> FunnelChart:
        return FunnelChartDashboard(
            instance=self.instance,
            dashboard_id=self.id,
            column=column_index,
            row=row_index,
            colspan=column_span,
            rowspan=row_span
        )

    def PyramidChart(
            self,
            column_index: int,
            row_index: int,
            column_span: int = 1,
            row_span: int = 1,
            title: str = None
    ) -> PyramidChart:
        return PyramidChartDashboard(
            instance=self.instance,
            dashboard_id=self.id,
            column=column_index,
            row=row_index,
            colspan=column_span,
            rowspan=row_span
        )


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class ZoomBandChart(Chart):
    """Chart that is attached to a single Axis of a ChartXY."""

    def __init__(
            self,
            instance: Instance,
            chart_id: str,
            dashboard_id: str,
            column_index: int,
            column_span: int,
            row_index: int,
            row_span: int,
            axis: Axis | str
    ):
        Chart.__init__(self, instance)
        self.instance.send_command(self.id, 'zoomBandChart', {
            'db': dashboard_id,
            'chart': chart_id,
            'column_index': column_index,
            'column_span': column_span,
            'row_index': row_index,
            'row_span': row_span,
            'axis': axis
        })


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class PieChart(OpenChart, GeneralMethods, TitleMethods, ChartWithLUT, ChartWithLabelStyling):

    def __init__(self, theme: str = None, labels_inside_slices: bool = False):
        """Visualizes proportions and percentages between categories, by dividing a circle into proportional segments.

        Args:
            labels_inside_slices (bool): If true, the labels are inside pie slices. If false, the labels are on the
                sides of the slices.

        Returns:
            Reference to Pie Chart class.
        """
        instance = lightningchart.Instance()
        Chart.__init__(self, instance)
        self.instance.send_command(self.id, 'pieChart', {
            'theme': theme,
            'labelsInsideSlices': labels_inside_slices
        })

    def add_slice(self, name: str, value: int | float):
        """Add new Slice to the Pie Chart.

        Args:
            name (str): Initial name for Slice as string.
            value (int): Initial value for Slice as number.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'addSlice', {
            'name': name,
            'value': value
        })
        return self

    def add_slices(self, slices: list[dict[str, int | float]]):
        """This method is used for the adding multiple slices in the funnel chart.

        Args:
            slices (list[dict[int | float, int | float]]): List of slices {name, value}.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'addSlices', {'slices': slices})
        return self

    def set_inner_radius(self, radius: int | float):
        """Set inner radius of Pie Chart.
        This method can be used to style the Pie Chart as a "Donut Chart", with the center being hollow.

        Args:
            radius (int | float): Inner radius as a percentage of outer radius [0, 100]

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setInnerRadius', {'radius': radius})
        return self

    def set_slice_stroke_style(
            self,
            thickness: int | float,
            color: tuple[int, int, int] | tuple[int, int, int, int] = (255, 255, 255, 255)):
        """Set stroke style of Pie Slices border.

        Args:
            thickness (int | float): Thickness of the slice border.
            color (tuple[int, int, int] | tuple[int, int, int, int]): Color of the slice border.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setSliceStrokeStyle', {'thickness': thickness, 'color': color})
        return self


class PieChartDashboard(PieChart):

    def __init__(
            self,
            instance: Instance,
            dashboard_id: str,
            column: int,
            row: int,
            colspan: int,
            rowspan: int):
        Chart.__init__(self, instance)
        self.instance.send_command(self.id, 'createPieChart', {
            'db': dashboard_id,
            'column': column,
            'row': row,
            'colspan': colspan,
            'rowspan': rowspan
        })


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class GaugeChart(OpenChart, GeneralMethods, TitleMethods, ChartWithLUT):

    def __init__(self, theme: str = None):
        """A Gauge Chart with a single solid colored slice.

        Returns:
            Reference to Gauge Chart class.
        """
        instance = lightningchart.Instance()
        Chart.__init__(self, instance)
        self.instance.send_command(self.id, 'gaugeChart', {'theme': theme})

    def set_angle_interval(self, start: int | float, end: int | float):
        """Set angular interval of the gauge in degrees.

        Args:
            start (int | float): Start angle of the gauge in degrees.
            end (int | float): Start angle of the gauge in degrees.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setAngleInterval', {
            'start': start,
            'end': end
        })
        return self

    def set_interval(self, start: int | float, end: int | float):
        """Set scale interval of the gauge slice.

        Args:
            start (int | float): Start scale value.
            end (int | float): End scale value.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setGaugeInterval', {'start': start, 'end': end})
        return self

    def set_value(self, value: int | float):
        """Set value of gauge slice.

        Args:
            value (int | float): Numeric value.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setGaugeValue', {'value': value})
        return self

    def set_thickness(self, thickness: int | float):
        """Set thickness of the gauge.

        Args:
            thickness (int | float): Thickness of the gauge.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setThickness', {'thickness': thickness})
        return self

    def set_gauge_color(self, rgba: tuple[int, int, int] | tuple[int, int, int, int] = (255, 255, 255, 255)):
        """Set the color of the underlying gauge arc, not the value slice.

        Args:
            rgba (tuple[int, int, int] | tuple[int, int, int, int]): Color of the gauge.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setGaugeColor', {'color': rgba})
        return self

    def set_slice_color(self, rgba: tuple[int, int, int] | tuple[int, int, int, int] = (255, 255, 255, 255)):
        """Set the color gauge value slice.

        Args:
            rgba (tuple[int, int, int] | tuple[int, int, int, int]): Color of the slice.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setFillStyle', {'color': rgba})
        return self

    def set_label_color(self, rgba: tuple[int, int, int] | tuple[int, int, int, int] = (255, 255, 255, 255)):
        """Set the color of gauge data label.

        Args:
            rgba (tuple[int, int, int] | tuple[int, int, int, int]): Color of the label.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setDataLabelFillStyle', {'color': rgba})
        return self

    def set_label_font(
            self,
            size: int | float = 20,
            family: str = 'Arial, Helvetica, sans-serif',
            weight: str = 'bold',
            style: str = 'italic',
    ):
        """Set font of gauge data labels.

        Args:
            size (int | float): CSS font size.
            family (str): CSS font family.
            weight (str): CSS font weight.
            style (str): CSS font style.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setDataLabelFont', {
            'size': size,
            'family': family,
            'weight': weight,
            'style': style
        })
        return self

    def set_highlight(self, highlight: float | bool = 1.0):
        """If highlight animations are enabled (which is true by default), the transition will be animated.
        As long as the component is highlighted, the active highlight intensity will be animated continuously
        between 0 and the configured value.

        Args:
            highlight (float | bool): Boolean or number between 0 and 1, where 1 is fully highlighted.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setGaugeHighlight', {'highlight': highlight})
        return self

    def set_gauge_stroke_style(
            self,
            thickness: int | float,
            color: tuple[int, int, int] | tuple[int, int, int, int] = (255, 255, 255, 255)):
        """Set stroke of gauge background.

        Args:
            thickness (int | float): Thickness of the slice border.
            color (tuple[int, int, int] | tuple[int, int, int, int]): Color of the slice border.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setGaugeStrokeStyle', {'thickness': thickness, 'color': color})
        return self


class GaugeChartDashboard(GaugeChart):

    def __init__(
            self,
            instance: Instance,
            dashboard_id: str,
            column: int,
            row: int,
            colspan: int,
            rowspan: int):
        Chart.__init__(self, instance)
        self.instance.send_command(self.id, 'createGaugeChart', {
            'db': dashboard_id,
            'column': column,
            'row': row,
            'colspan': colspan,
            'rowspan': rowspan
        })


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class FunnelChart(OpenChart, GeneralMethods, TitleMethods, ChartWithLUT, ChartWithLabelStyling):

    def __init__(self, theme: str = None):
        """Visualizes proportions and percentages between categories, by dividing a funnel into proportional segments.

        Returns:
            Reference to Funnel Chart class.
        """
        instance = lightningchart.Instance()
        Chart.__init__(self, instance)
        self.instance.send_command(self.id, 'funnelChart', {'theme': theme})

    def add_slice(self, name: str, value: int | float):
        """This method is used for the adding slices in the funnel chart.

        Args:
            name (str): Funnel slice title.
            value (int | float): Funnel slice value.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'addSlice', {'name': name, 'value': value})
        return self

    def add_slices(self, slices: list[dict[str, int | float]]):
        """This method is used for the adding multiple slices in the funnel chart.

        Args:
            slices (list[dict[str, int | float]]): Array of {name, value} slices.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'addSlices', {'slices': slices})
        return self

    def set_head_width(self, width: int | float):
        """Set Funnel Head Width.

        Args:
            width (int | float): Funnel Head Width range from 0 to 100.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setHeadWidth', {'width': width})
        return self

    def set_neck_width(self, width: int | float):
        """Set Funnel Neck Width.

        Args:
            width (int | float): Funnel Neck Width range from 0 to 100.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setNeckWidth', {'width': width})
        return self

    def set_slice_mode(self, mode: str = 'height'):
        """Set FunnelSliceMode. Can be used to select between different drawing approaches for Slices.

        Args:
            mode (str): "height" | "width"

        Returns:
            Reference to self.
        """
        if mode.lower().startswith('width'):
            mode = 1
        else:
            mode = 0
        self.instance.send_command(self.id, 'setSliceMode', {'mode': mode})
        return self

    def set_slice_gap(self, gap: int | float):
        """Set gap between Slice / start of label connector, and end of label connector / Label.

        Args:
            gap (int | float): Gap as pixels. Clamped between [0, 20] !

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setSliceGap', {'gap': gap})
        return self

    def set_slice_stroke_style(
            self,
            thickness: int | float,
            color: tuple[int, int, int] | tuple[int, int, int, int] = (255, 255, 255, 255)):
        """Set stroke style of Funnel Slices border.

        Args:
            thickness (int | float): Thickness of the slice border.
            color (tuple[int, int, int] | tuple[int, int, int, int]): Color of the slice border.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setSliceStrokeStyle', {'thickness': thickness, 'color': color})
        return self


class FunnelChartDashboard(FunnelChart):
    def __init__(
            self,
            instance: Instance,
            dashboard_id: str,
            column: int,
            row: int,
            colspan: int,
            rowspan: int):
        Chart.__init__(self, instance)
        self.instance.send_command(self.id, 'createFunnelChart', {
            'db': dashboard_id,
            'column': column,
            'row': row,
            'colspan': colspan,
            'rowspan': rowspan
        })


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class PyramidChart(OpenChart, GeneralMethods, TitleMethods, ChartWithLUT, ChartWithLabelStyling):

    def __init__(self, theme: str = None):
        """Visualizes proportions and percentages between categories, by dividing a pyramid into proportional segments.

        Returns:
            Reference to Pyramid Chart class.
        """
        instance = lightningchart.Instance()
        Chart.__init__(self, instance)
        self.instance.send_command(self.id, 'pyramidChart', {'theme': theme})

    def add_slice(self, name: str, value: int | float):
        """This method is used for the adding slices in the pyramid chart.

        Args:
            name (str): Pyramid slice title.
            value (int | flaot): Pyramid slice value.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'addSlice', {'name': name, 'value': value})
        return self

    def add_slices(self, slices: list[dict[str, int | float]]):
        """This method is used for the adding multiple slices in the pyramid chart.

        Args:
            slices (list[dict[str, int | float]]): Array of {name, value} slices.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'addSlices', {'slices': slices})
        return self

    def set_neck_width(self, width: int | float):
        """Set Pyramid Neck Width.

        Args:
            width (int | float): Pyramid Neck Width range from 0 to 100.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setNeckWidth', {'width': width})
        return self

    def set_slice_mode(self, mode: str = 'height'):
        """Set PyramidSliceMode. Can be used to select between different drawing approaches for Slices.

        Args:
            mode (str): "height" | "width"

        Returns:
            Reference to self.
        """
        if mode.lower().startswith('width'):
            mode = 1
        else:
            mode = 0
        self.instance.send_command(self.id, 'setSliceMode', {'mode': mode})
        return self

    def set_slice_gap(self, gap: int | float):
        """Set gap between Slice / start of label connector, and end of label connector / Label.

        Args:
            gap (int | float): Gap as pixels. Clamped between [0, 20] !

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setSliceGap', {'gap': gap})
        return self

    def set_slice_stroke_style(
            self,
            thickness: int | float,
            color: tuple[int, int, int] | tuple[int, int, int, int] = (255, 255, 255, 255)):
        """Set stroke style of Pyramid Slices border.

        Args:
            thickness (int | float): Thickness of the slice border.
            color (tuple[int, int, int] | tuple[int, int, int, int]): Color of the slice border.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setSliceStrokeStyle', {'thickness': thickness, 'color': color})
        return self


class PyramidChartDashboard(PyramidChart):
    def __init__(
            self,
            instance: Instance,
            dashboard_id: str,
            column: int,
            row: int,
            colspan: int,
            rowspan: int):
        Chart.__init__(self, instance)
        self.instance.send_command(self.id, 'createPyramidChart', {
            'db': dashboard_id,
            'column': column,
            'row': row,
            'colspan': colspan,
            'rowspan': rowspan
        })


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class SpiderChart(GeneralMethods, TitleMethods):

    def __init__(self, instance: Instance):
        Chart.__init__(self, instance)
        self.instance.send_command(self.id, '', {})

    def add_axis(self):
        pass

    def add_series(self):
        pass

    def set_auto_axis(self):
        pass

    def set_auto_cursor(self):
        pass

    def set_auto_cursor_mode(self):
        pass

    def set_axis_interval(self):
        pass

    def set_axis_label_effect(self):
        pass

    def set_axis_label_font(self):
        pass

    def set_axis_label_strategy(self):
        pass

    def set_axis_label_color(self):
        pass

    def set_axis_scroll_strategy(self):
        pass

    def set_axis_style(self):
        pass

    def set_mouse_interactions(self):
        pass

    def set_nib_length(self):
        pass

    def set_nib_style(self):
        pass

    def set_series_background_effect(self):
        pass

    def set_series_background_color(self):
        pass

    def set_series_background_stroke_style(self):
        pass

    def set_web_count(self):
        pass

    def set_web_mode(self):
        pass

    def set_web_style(self):
        pass


class SpiderChartDashboard(SpiderChart):
    def __init__(
            self,
            instance: Instance,
            dashboard_id: str,
            column: int,
            row: int,
            colspan: int,
            rowspan: int):
        Chart.__init__(self, instance)
        self.instance.send_command(self.id, 'createSpiderChart', {
            'db': dashboard_id,
            'column': column,
            'row': row,
            'colspan': colspan,
            'rowspan': rowspan
        })


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class PolarChart(GeneralMethods, TitleMethods):

    def __init__(self, instance: Instance):
        Chart.__init__(self, instance)
        self.instance.send_command(self.id, '', {})

    def add_area_series(self):
        pass

    def add_line_series(self):
        pass

    def add_point_line_series(self):
        pass

    def add_point_series(self):
        pass

    def add_polygon_series(self):
        pass

    def add_sector(self):
        pass

    def set_auto_cursor_mode(self):
        pass


class PolarChartDashboard(PolarChart):
    def __init__(
            self,
            instance: Instance,
            dashboard_id: str,
            column: int,
            row: int,
            colspan: int,
            rowspan: int):
        Chart.__init__(self, instance)
        self.instance.send_command(self.id, 'createPolarChart', {
            'db': dashboard_id,
            'column': column,
            'row': row,
            'colspan': colspan,
            'rowspan': rowspan
        })


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class MapChart(GeneralMethods, TitleMethods):

    def __init__(self, instance: Instance):
        Chart.__init__(self, instance)
        self.instance.send_command(self.id, '', {})


class MapChartDashboard(MapChart):
    def __init__(
            self,
            instance: Instance,
            dashboard_id: str,
            column: int,
            row: int,
            colspan: int,
            rowspan: int):
        Chart.__init__(self, instance)
        self.instance.send_command(self.id, 'createMapChart', {
            'db': dashboard_id,
            'column': column,
            'row': row,
            'colspan': colspan,
            'rowspan': rowspan
        })


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class DataGrid(GeneralMethods, TitleMethods):

    def __init__(self, instance: Instance):
        Chart.__init__(self, instance)
        self.instance.send_command(self.id, '', {})


class DataGridDashboard(DataGrid):
    def __init__(
            self,
            instance: Instance,
            dashboard_id: str,
            column: int,
            row: int,
            colspan: int,
            rowspan: int):
        Chart.__init__(self, instance)
        self.instance.send_command(self.id, 'createDataGrid', {
            'db': dashboard_id,
            'column': column,
            'row': row,
            'colspan': colspan,
            'rowspan': rowspan
        })


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class UIPanel(GeneralMethods):

    def __init__(self, instance: Instance):
        Chart.__init__(self, instance)
        self.instance.send_command(self.id, '', {})


class UIPanelDashboard(UIPanel):
    def __init__(
            self,
            instance: Instance,
            dashboard_id: str,
            column: int,
            row: int,
            colspan: int,
            rowspan: int):
        Chart.__init__(self, instance)
        self.instance.send_command(self.id, 'createUIPanel', {
            'db': dashboard_id,
            'column': column,
            'row': row,
            'colspan': colspan,
            'rowspan': rowspan
        })


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
