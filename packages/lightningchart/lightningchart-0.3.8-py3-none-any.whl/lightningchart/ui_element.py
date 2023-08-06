from __future__ import annotations
import uuid

import lightningchart.charts


class UIElement:
    """Base class which all UI elements will inherit."""

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

    def set_visible(self, visible: bool = True):
        """Set element visibility.

        Args:
            visible (bool): True when element should be visible and false when element should be hidden.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setVisible', {'visible': int(visible)})
        return self


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class UIEWithPosition(UIElement):
    """Prototype class for UI element with adjustable position."""

    def set_position(self, x: int, y: int):
        """Sets the position of this UiElement relative to its origin

        Args:
            x (int): Location in X-dimension.
            y (int): Location in Y-dimension.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setPosition', {'x': x, 'y': y})
        return self


class UIEWithTitle(UIElement):
    """Prototype class for UI element with title."""

    def set_title(self, title: str):
        """Set text of LegendBox title.

        Args:
            title (str): LegendBox title as a string.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setTitle', {'title': title})
        return self


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class Axis(UIEWithTitle):
    """Base class for chart axes, used to create custom axes."""

    def __init__(
            self,
            chart: lightningchart.charts.Chart,
            axis: str,
            opposite: bool,
            type: str,
            base: int
    ):
        UIElement.__init__(self, chart)
        self.instance.send_command(self.id, 'addAxis', {
            'chart': self.chart.id,
            'axis': axis,
            'opposite': opposite,
            'type': type,
            'base': base
        })

    def set_visible(self, visible: bool = True):
        """Set element visibility.

                Args:
                    visible (bool): True when element should be visible and false when element should be hidden.

                Returns:
                    Reference to self.
                """
        self.instance.send_command(self.chart.id, 'setVisibleAxis', {
            'axis': self.id,
            'visible': int(visible)
        })
        return self

    def set_tick_strategy(self, strategy: str = 'time', time_origin: int | float = None):
        """Set TickStrategy of Axis. The TickStrategy defines the positioning and formatting logic of Axis ticks
        as well as the style of created ticks.

        Args:
            strategy (str): "Empty" | "Numeric" | "DateTime" | "Time"
            time_origin (int | float): Define with time.time(). If a time origin is defined,
                data-points will instead be interpreted as milliseconds since time origin.

        Returns:
            Reference to self.
        """
        if strategy.lower().startswith('time'):
            strategy = 'Time'
        elif strategy.lower().startswith('date'):
            strategy = 'DateTime'
        elif strategy.lower().startswith('num'):
            strategy = 'Numeric'
        else:
            strategy = 'Empty'

        self.instance.send_command(self.chart.id, 'setTickStrategy', {
            'strategy': strategy,
            'axis': self.id,
            'timeOrigin': time_origin
        })
        return self

    def set_scroll_strategy(self, strategy: str = 'progressive'):
        """Specify ScrollStrategy of the Axis.
        This decides where the Axis scrolls based on current view and series boundaries.

        Args:
            strategy (str):  "expansion" | "fitting" | "progressive" | "regressive"

        Returns:
            Reference to self.
        """
        if strategy.lower().startswith('ex'):
            strategy = 'expansion'
        elif strategy.lower().startswith('fit'):
            strategy = 'fitting'
        elif strategy.lower().startswith('reg'):
            strategy = 'regressive'
        elif strategy.lower().startswith('prog'):
            strategy = 'progressive'
        else:
            raise Exception('Invalid strategy type')

        self.instance.send_command(self.chart.id, 'setScrollStrategy', {
            'strategy': strategy,
            'axis': self.id
        })
        return self

    def set_interval(
            self,
            start: int,
            end: int,
            stop_axis_after: bool = False,
            animate: bool = False
    ):
        """Set axis interval.

        Args:
            start (int): Start of the axis.
            end (int): End of the axis.
            stop_axis_after (bool): If false, the axis won't stop from scrolling.
            animate (bool): Boolean for animation enabled, or number for animation duration in milliseconds.

        Returns:
            Reference to self.
        """

        self.instance.send_command(self.chart.id, 'setAxisInterval', {
            'start': start,
            'end': end,
            'axis': self.id,
            'stop': int(stop_axis_after),
            'animate': animate
        })
        return self


class DefaultAxis(Axis):
    """Class for default chart axes."""

    def __init__(self, chart: lightningchart.charts.Chart, axis: str):
        self.chart = chart
        self.id = axis
        self.instance = chart.instance

    def dispose(self):
        """Permanently destroy the component.

        Returns:
            True
        """
        self.instance.send_command(self.chart.id, 'disposeDefaultAxis', {'axis': self.id})
        return True


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class ChartMarker(UIEWithPosition):
    """Class for markers within a chart."""

    def __init__(self, chart: lightningchart.charts.Chart, x: int, y: int):
        UIElement.__init__(self, chart)
        self.instance.send_command(self.id, 'addChartMarkerXY', {'chart': self.chart.id})
        if x and y:
            self.set_position(x, y)

    def set_visibility(self, visibility: str = 'always'):
        """Set visibility mode for PointMarker. PointMarker is a visual that is displayed at the Cursors position.

        Args:
            visibility (str): "always" | "never" | "whenDragged" | "whenHovered" | "whenHoveredOrDragged"
            | "whenNotDragged"

        Returns:
            Reference for self.
        """
        self.instance.send_command(self.id, 'setPointMarkerVisibility', {'visibility': visibility})
        return self

    def set_dragging_mode(self, mode: str = 'draggable'):
        """Set dragging mode of object. Defines how the object can be dragged by mouse.

        Args:
            mode (str): "draggable" | "notDraggable" | "onlyHorizontal" | "onlyVertical"

        Returns:
            Reference for self.
        """
        self.instance.send_command(self.id, 'setDraggingMode', {'mode': mode})
        return self


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class Legend(UIEWithPosition, UIEWithTitle):
    """Class for legend boxes in a chart."""

    def __init__(
            self,
            chart: lightningchart.charts.Chart,
            horizontal: bool = False,
            title: str = None,
            data=None,
            x: int = None,
            y: int = None
    ):
        UIElement.__init__(self, chart)
        self.instance.send_command(self.id, 'legend', {
            'chart': chart.id,
            'horizontal': horizontal
        })
        if title:
            self.set_title(title)
        if data:
            self.add(data)
        if x and y:
            self.set_position(x, y)

    def __str__(self):
        return 'Legend'

    def add(self, data):
        """Add a dynamic value to LegendBox, creating a group and entries for it depending on type of value.
        Supports series, charts and dashboards.

        Args:
            data: Series, Chart or Dashboard

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'legendAdd', {'chart': data.id})
        return self


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class TextBox(UIEWithPosition):

    def __init__(
            self,
            chart: lightningchart.charts.Chart,
            text: str = None,
            x: int = None,
            y: int = None
    ):
        UIElement.__init__(self, chart)
        self.instance.send_command(self.id, 'textBox', {'chart': self.chart.id})

        if text:
            self.set_text(text)
        if x and y:
            self.set_position(x, y)

    def __str__(self):
        return 'TextBox'

    def set_text(self, text: str):
        """Set the text of the entire shape.

        Args:
            text (str): Text string.

        Returns:
            Reference to self.
        """
        self.instance.send_command(self.id, 'setText', {'text': text})
        return self
