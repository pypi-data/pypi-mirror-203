var lcjsThemes = (function (exports, lcjs) {
    'use strict';

    var colorMissing = lcjs.ColorRGBA(0, 255, 0);
    var StylePalette = function (array, clbk) {
      var values = array.map(clbk);
      return function (i) {
        return values[i % values.length];
      };
    };
    /**
     * Factory function for creating a LightningChart JS Theme with a flat style based on very minimal configuration options.
     * @param   options - Configuration options for the created theme.
     * @returns
     */
    var makeFlatTheme = function (options) {
      var whiteFillStyle = new lcjs.SolidFill({
        color: lcjs.ColorRGBA(255, 255, 255)
      });
      var blackFillStyle = new lcjs.SolidFill({
        color: lcjs.ColorRGBA(0, 0, 0)
      });
      //
      //
      //
      var isDark = options.isDark !== undefined ? options.isDark : true;
      var lcjsBackgroundFillStyle = new lcjs.SolidFill({
        color: options.backgroundColor
      });
      var highlightColorOffset = isDark ? lcjs.ColorRGBA(60, 60, 60, 60) : lcjs.ColorRGBA(-60, -60, -60, 60);
      var highlightColorOffsetAxisOverlay = isDark ? lcjs.ColorRGBA(255, 255, 255, 40) : lcjs.ColorRGBA(0, 0, 0, 40);
      var dashboardSplitterStyle = new lcjs.SolidLine({
        thickness: 4,
        fillStyle: new lcjs.SolidFill({
          color: options.dashboardSplitterColor || colorMissing
        })
      });
      var chartBackgroundFillStyle = lcjsBackgroundFillStyle;
      var seriesBackgroundFillStyle = lcjs.transparentFill;
      var fontChartTitles = new lcjs.FontSettings({
        size: 18,
        family: options.fontFamily,
        weight: 'normal',
        style: 'normal'
      });
      var fontAxisTitles = new lcjs.FontSettings({
        size: 16,
        family: options.fontFamily,
        weight: 'normal',
        style: 'normal'
      });
      var fontLegendTitle = new lcjs.FontSettings({
        size: 14,
        family: options.fontFamily,
        weight: 'normal',
        style: 'normal'
      });
      var fontOther = new lcjs.FontSettings({
        size: 14,
        family: options.fontFamily,
        weight: 'normal',
        style: 'normal'
      });
      var textFillStyle = new lcjs.SolidFill({
        color: options.textColor
      });
      var zoomRectangleFillStyle = new lcjs.SolidFill({
        color: isDark ? lcjs.ColorRGBA(255, 255, 255, 20) : lcjs.ColorRGBA(0, 0, 0, 20)
      });
      var zoomRectangleStrokeStyle = new lcjs.SolidLine({
        thickness: 1,
        fillStyle: isDark ? whiteFillStyle : blackFillStyle
      });
      var primaryDataFillStyle = new lcjs.SolidFill({
        color: options.dataColors[0]
      });
      var dataSolidFillPalette = StylePalette(options.dataColors, function (color) {
        return new lcjs.SolidFill({
          color: color
        });
      });
      var dataSolidLinePalette = StylePalette(options.dataColors, function (color) {
        return new lcjs.SolidLine({
          fillStyle: new lcjs.SolidFill({
            color: color
          }),
          thickness: 2
        });
      });
      var dataAreaSolidFillPalette = StylePalette(options.dataColors, function (color) {
        return new lcjs.SolidFill({
          color: color.setA(100)
        });
      });
      var seriesStrokeStylePalette = dataSolidLinePalette;
      var seriesFillStylePalette = dataSolidFillPalette;
      var areaSeriesFillStylePalette = dataAreaSolidFillPalette;
      var dataBorderStrokePalette = dataSolidLinePalette;
      var pointSeries3DPointStylePalette = StylePalette(options.dataColors, function (color) {
        return new lcjs.PointStyle3D.Triangulated({
          shape: 'sphere',
          size: 10,
          fillStyle: new lcjs.SolidFill({
            color: color
          })
        });
      });
      var pointCloudSeries3DPointStylePalette = StylePalette(options.dataColors, function (color) {
        return new lcjs.PointStyle3D.Pixelated({
          size: 5,
          fillStyle: new lcjs.SolidFill({
            color: color
          })
        });
      });
      var dataFillStylePositive = new lcjs.SolidFill({
        color: lcjs.ColorRGBA(176, 255, 157)
      });
      var dataFillStyleNegative = new lcjs.SolidFill({
        color: lcjs.ColorRGBA(255, 112, 76)
      });
      var wireframeStyle = new lcjs.SolidLine({
        thickness: 1,
        fillStyle: blackFillStyle
      });
      var axisStrokeStyle = new lcjs.SolidLine({
        thickness: 1,
        fillStyle: new lcjs.SolidFill({
          color: options.axisColor
        })
      });
      var axisOverlayStyle = new lcjs.SolidFill({
        color: lcjs.ColorRGBA(0, 0, 0, 1)
      }); // NOTE: Slight opaqueness is required for this overlay becoming visible when highlighted.
      var tickStyle = new lcjs.VisibleTicks({
        gridStrokeStyle: new lcjs.SolidLine({
          thickness: 1,
          fillStyle: new lcjs.SolidFill({
            color: options.gridLineColor
          })
        }),
        tickStyle: lcjs.emptyLine,
        tickLength: 7,
        tickPadding: 0,
        labelFont: fontOther,
        labelPadding: 0,
        labelFillStyle: textFillStyle
      });
      var numericTickStrategy = new lcjs.NumericTickStrategy({
        extremeTickStyle: lcjs.emptyTick,
        majorTickStyle: tickStyle,
        minorTickStyle: tickStyle
      });
      var dateTimeTickStrategy = new lcjs.DateTimeTickStrategy({
        greatTickStyle: tickStyle.setTickLength(50).setTickPadding(-14),
        majorTickStyle: tickStyle,
        minorTickStyle: tickStyle
      });
      var timeTickStrategy = new lcjs.TimeTickStrategy({
        majorTickStyle: tickStyle,
        minorTickStyle: tickStyle
      });
      var cursorGridStrokeStyle = new lcjs.SolidLine({
        thickness: 1,
        fillStyle: isDark ? whiteFillStyle : blackFillStyle
      });
      var bandFillStyle = zoomRectangleFillStyle;
      var bandStrokeStyle = zoomRectangleStrokeStyle;
      var constantLineStrokeStyle = cursorGridStrokeStyle;
      var uiButtonFillStyle = isDark ? whiteFillStyle : blackFillStyle;
      var uiBackgroundFillStyle = new lcjs.SolidFill({
        color: options.uiBackgroundColor
      });
      var uiBackgroundStrokeStyle = new lcjs.SolidLine({
        thickness: 1,
        fillStyle: new lcjs.SolidFill({
          color: options.uiBorderColor
        })
      });
      var flatTheme = {
        isDark: isDark,
        effect: undefined,
        effectsText: false,
        effectsDashboardSplitters: false,
        lcjsBackgroundFillStyle: lcjsBackgroundFillStyle,
        lcjsBackgroundStrokeStyle: lcjs.emptyLine,
        highlightColorOffset: highlightColorOffset,
        highlightColorOffsetAxisOverlay: highlightColorOffsetAxisOverlay,
        dashboardSplitterStyle: dashboardSplitterStyle,
        chartXYBackgroundFillStyle: chartBackgroundFillStyle,
        chartXYBackgroundStrokeStyle: lcjs.emptyLine,
        chartXYTitleFont: fontChartTitles,
        chartXYTitleFillStyle: textFillStyle,
        chartXYSeriesBackgroundFillStyle: seriesBackgroundFillStyle,
        chartXYSeriesBackgroundStrokeStyle: lcjs.emptyLine,
        chartXYZoomingRectangleFillStyle: zoomRectangleFillStyle,
        chartXYZoomingRectangleStrokeStyle: zoomRectangleStrokeStyle,
        chartXYFittingRectangleFillStyle: zoomRectangleFillStyle,
        chartXYFittingRectangleStrokeStyle: zoomRectangleStrokeStyle,
        lineSeriesStrokeStyle: seriesStrokeStylePalette,
        pointLineSeriesStrokeStyle: seriesStrokeStylePalette,
        pointLineSeriesFillStyle: seriesFillStylePalette,
        pointSeriesFillStyle: seriesFillStylePalette,
        ellipseSeriesFillStyle: seriesFillStylePalette,
        ellipseSeriesStrokeStyle: seriesStrokeStylePalette,
        polygonSeriesFillStyle: seriesFillStylePalette,
        polygonSeriesStrokeStyle: seriesStrokeStylePalette,
        rectangleSeriesFillStyle: seriesFillStylePalette,
        rectangleSeriesStrokeStyle: lcjs.emptyLine,
        segmentSeriesStrokeStyle: seriesStrokeStylePalette,
        boxSeriesBodyFillStyle: seriesFillStylePalette(0),
        boxSeriesBodyStrokeStyle: lcjs.emptyLine,
        boxSeriesStrokeStyle: new lcjs.SolidLine({
          thickness: 1,
          fillStyle: isDark ? whiteFillStyle : blackFillStyle
        }),
        boxSeriesMedianStrokeStyle: new lcjs.SolidLine({
          thickness: 1,
          fillStyle: isDark ? blackFillStyle : whiteFillStyle
        }),
        ohlcCandleBodyFillStylePositive: dataFillStylePositive,
        ohlcCandleBodyFillStyleNegative: dataFillStyleNegative,
        ohlcCandleBodyStrokeStylePositive: lcjs.emptyLine,
        ohlcCandleBodyStrokeStyleNegative: lcjs.emptyLine,
        ohlcCandleStrokeStyle: new lcjs.SolidLine({
          thickness: 1,
          fillStyle: isDark ? whiteFillStyle : blackFillStyle
        }),
        ohlcBarStrokeStylePositive: new lcjs.SolidLine({
          thickness: 2,
          fillStyle: dataFillStylePositive
        }),
        ohlcBarStrokeStyleNegative: new lcjs.SolidLine({
          thickness: 2,
          fillStyle: dataFillStyleNegative
        }),
        heatmapGridSeriesFillStyle: seriesFillStylePalette,
        heatmapGridSeriesWireframeStyle: wireframeStyle,
        heatmapScrollingGridSeriesFillStyle: seriesFillStylePalette,
        heatmapScrollingGridSeriesWireframeStyle: wireframeStyle,
        areaRangeSeriesFillStyle: areaSeriesFillStylePalette,
        areaRangeSeriesStrokeStyle: dataBorderStrokePalette,
        areaRangeSeriesFillStyleInverted: areaSeriesFillStylePalette,
        areaRangeSeriesStrokeStyleInverted: dataBorderStrokePalette,
        areaSeriesBipolarHighFillStyle: areaSeriesFillStylePalette,
        areaSeriesBipolarHighStrokeStyle: dataBorderStrokePalette,
        areaSeriesBipolarLowFillStyle: areaSeriesFillStylePalette,
        areaSeriesBipolarLowStrokeStyle: dataBorderStrokePalette,
        areaSeriesPositiveFillStyle: areaSeriesFillStylePalette,
        areaSeriesPositiveStrokeStyle: dataBorderStrokePalette,
        areaSeriesNegativeFillStyle: areaSeriesFillStylePalette,
        areaSeriesNegativeStrokeStyle: dataBorderStrokePalette,
        xAxisTitleFont: fontAxisTitles,
        xAxisTitleFillStyle: textFillStyle,
        xAxisStrokeStyle: axisStrokeStyle,
        xAxisNibStyle: lcjs.emptyLine,
        xAxisOverlayStyle: axisOverlayStyle,
        xAxisZoomingBandFillStyle: zoomRectangleFillStyle,
        xAxisZoomingBandStrokeStyle: lcjs.emptyLine,
        xAxisNumericTicks: numericTickStrategy,
        xAxisDateTimeTicks: dateTimeTickStrategy,
        xAxisTimeTicks: timeTickStrategy,
        yAxisTitleFont: fontAxisTitles,
        yAxisTitleFillStyle: textFillStyle,
        yAxisStrokeStyle: axisStrokeStyle,
        yAxisNibStyle: lcjs.emptyLine,
        yAxisOverlayStyle: axisOverlayStyle,
        yAxisZoomingBandFillStyle: zoomRectangleFillStyle,
        yAxisZoomingBandStrokeStyle: lcjs.emptyLine,
        yAxisNumericTicks: numericTickStrategy,
        yAxisDateTimeTicks: dateTimeTickStrategy,
        yAxisTimeTicks: timeTickStrategy,
        bandFillStyle: bandFillStyle,
        bandStrokeStyle: bandStrokeStyle,
        constantLineStrokeStyle: constantLineStrokeStyle,
        chart3DBackgroundFillStyle: chartBackgroundFillStyle,
        chart3DBackgroundStrokeStyle: lcjs.emptyLine,
        chart3DTitleFont: fontChartTitles,
        chart3DTitleFillStyle: textFillStyle,
        chart3DSeriesBackgroundFillStyle: seriesBackgroundFillStyle,
        chart3DSeriesBackgroundStrokeStyle: lcjs.emptyLine,
        chart3DBoundingBoxStrokeStyle: lcjs.emptyLine,
        xAxis3DTitleFont: fontAxisTitles,
        xAxis3DTitleFillStyle: textFillStyle,
        xAxis3DStrokeStyle: axisStrokeStyle,
        xAxis3DNumericTicks: numericTickStrategy,
        xAxis3DDateTimeTicks: dateTimeTickStrategy,
        xAxis3DTimeTicks: timeTickStrategy,
        yAxis3DTitleFont: fontAxisTitles,
        yAxis3DTitleFillStyle: textFillStyle,
        yAxis3DStrokeStyle: axisStrokeStyle,
        yAxis3DNumericTicks: numericTickStrategy,
        yAxis3DDateTimeTicks: dateTimeTickStrategy,
        yAxis3DTimeTicks: timeTickStrategy,
        zAxis3DTitleFont: fontAxisTitles,
        zAxis3DTitleFillStyle: textFillStyle,
        zAxis3DStrokeStyle: axisStrokeStyle,
        zAxis3DNumericTicks: numericTickStrategy,
        zAxis3DDateTimeTicks: dateTimeTickStrategy,
        zAxis3DTimeTicks: timeTickStrategy,
        lineSeries3DStrokeStyle: seriesStrokeStylePalette,
        pointLineSeries3DStrokeStyle: seriesStrokeStylePalette,
        pointLineSeries3DPointStyle: pointSeries3DPointStylePalette,
        pointSeries3DPointStyle: pointSeries3DPointStylePalette,
        pointCloudSeries3DPointStyle: pointCloudSeries3DPointStylePalette,
        surfaceGridSeries3DFillStyle: seriesFillStylePalette,
        surfaceGridSeries3DWireframeStyle: wireframeStyle,
        surfaceScrollingGridSeries3DFillStyle: seriesFillStylePalette,
        surfaceScrollingGridSeries3DWireframeStyle: wireframeStyle,
        boxSeries3DFillStyle: seriesFillStylePalette,
        polarChartBackgroundFillStyle: chartBackgroundFillStyle,
        polarChartBackgroundStrokeStyle: lcjs.emptyLine,
        polarChartTitleFont: fontChartTitles,
        polarChartTitleFillStyle: textFillStyle,
        polarChartSeriesBackgroundFillStyle: seriesBackgroundFillStyle,
        polarChartSeriesBackgroundStrokeStyle: lcjs.emptyLine,
        polarSectorFillStyle: bandFillStyle,
        polarSectorStrokeStyle: bandStrokeStyle,
        polarAmplitudeAxisTitleFont: fontAxisTitles,
        polarAmplitudeAxisTitleFillStyle: textFillStyle,
        polarAmplitudeAxisStrokeStyle: axisStrokeStyle,
        polarAmplitudeAxisNumericTicks: numericTickStrategy,
        polarAmplitudeAxisDateTimeTicks: dateTimeTickStrategy,
        polarAmplitudeAxisTimeTicks: timeTickStrategy,
        polarRadialAxisTitleFont: fontAxisTitles,
        polarRadialAxisTitleFillStyle: textFillStyle,
        polarRadialAxisStrokeStyle: axisStrokeStyle,
        polarRadialAxisTickStyle: tickStyle,
        polarLineSeriesStrokeStyle: seriesStrokeStylePalette,
        polarPointLineSeriesFillStyle: seriesFillStylePalette,
        polarPointLineSeriesStrokeStyle: seriesStrokeStylePalette,
        polarPointSeriesFillStyle: seriesFillStylePalette,
        polarPolygonSeriesFillStyle: areaSeriesFillStylePalette,
        polarPolygonSeriesStrokeStyle: dataBorderStrokePalette,
        polarAreaSeriesFillStyle: areaSeriesFillStylePalette,
        polarAreaSeriesStrokeStyle: dataBorderStrokePalette,
        mapChartBackgroundFillStyle: chartBackgroundFillStyle,
        mapChartBackgroundStrokeStyle: lcjs.emptyLine,
        mapChartTitleFont: fontChartTitles,
        mapChartTitleFillStyle: textFillStyle,
        mapChartFillStyle: primaryDataFillStyle,
        mapChartStrokeStyle: new lcjs.SolidLine({
          thickness: 1,
          fillStyle: blackFillStyle
        }),
        mapChartOutlierRegionFillStyle: lcjs.emptyFill,
        mapChartOutlierRegionStrokeStyle: new lcjs.SolidLine({
          thickness: 1,
          fillStyle: isDark ? whiteFillStyle : blackFillStyle
        }),
        mapChartSeparateRegionFillStyle: uiBackgroundFillStyle,
        mapChartSeparateRegionStrokeStyle: uiBackgroundStrokeStyle,
        dataGridBackgroundFillStyle: chartBackgroundFillStyle,
        dataGridBackgroundStrokeStyle: lcjs.emptyLine,
        dataGridTitleFont: fontChartTitles,
        dataGridTitleFillStyle: textFillStyle,
        dataGridTextFont: fontOther,
        dataGridTextFillStyle: textFillStyle,
        dataGridCellBackgroundFillStyle: seriesBackgroundFillStyle,
        dataGridBorderStrokeStyle: uiBackgroundStrokeStyle,
        dataGridScrollBarBackgroundFillStyle: new lcjs.SolidFill({
          color: lcjs.ColorRGBA(30, 30, 30)
        }),
        dataGridScrollBarBackgroundStrokeStyle: lcjs.emptyLine,
        dataGridScrollBarFillStyle: new lcjs.SolidFill({
          color: lcjs.ColorRGBA(30, 30, 30)
        }),
        dataGridScrollBarStrokeStyle: uiBackgroundStrokeStyle,
        dataGridScrollBarButtonFillStyle: new lcjs.SolidFill({
          color: lcjs.ColorRGBA(30, 30, 30)
        }),
        dataGridScrollBarButtonStrokeStyle: uiBackgroundStrokeStyle,
        dataGridScrollBarButtonArrowFillStyle: uiButtonFillStyle,
        dataGridScrollBarButtonArrowStrokeStyle: lcjs.emptyLine,
        sparkLineChartStrokeStyle: seriesStrokeStylePalette(0),
        sparkPointChartFillStyle: seriesFillStylePalette(0),
        sparkBarChartFillStyle: seriesFillStylePalette(0),
        sparkBarChartStrokeStyle: dataBorderStrokePalette(0),
        sparkAreaChartFillStyle: areaSeriesFillStylePalette(0),
        sparkAreaChartStrokeStyle: dataBorderStrokePalette(0),
        sparkPieChartFillStyle: seriesFillStylePalette,
        sparkPieChartStrokeStyle: uiBackgroundStrokeStyle,
        sparkChartBandFillStyle: bandFillStyle,
        sparkChartBandStrokeStyle: bandStrokeStyle,
        sparkChartConstantLineStrokeStyle: constantLineStrokeStyle,
        spiderChartBackgroundFillStyle: chartBackgroundFillStyle,
        spiderChartBackgroundStrokeStyle: lcjs.emptyLine,
        spiderChartTitleFont: fontChartTitles,
        spiderChartTitleFillStyle: textFillStyle,
        spiderChartSeriesBackgroundFillStyle: seriesBackgroundFillStyle,
        spiderChartSeriesBackgroundStrokeStyle: lcjs.emptyLine,
        spiderChartWebStyle: tickStyle.gridStrokeStyle,
        spiderChartScaleLabelFillStyle: textFillStyle,
        spiderChartScaleLabelFont: fontOther,
        spiderChartAxisLabelFillStyle: textFillStyle,
        spiderChartAxisLabelFont: fontAxisTitles,
        spiderChartAxisStrokeStyle: axisStrokeStyle,
        spiderChartAxisNibStrokeStyle: lcjs.emptyLine,
        spiderSeriesFillStyle: areaSeriesFillStylePalette,
        spiderSeriesStrokeStyle: dataBorderStrokePalette,
        spiderSeriesPointFillStyle: seriesFillStylePalette,
        pieChartBackgroundFillStyle: chartBackgroundFillStyle,
        pieChartBackgroundStrokeStyle: lcjs.emptyLine,
        pieChartTitleFont: fontAxisTitles,
        pieChartTitleFillStyle: textFillStyle,
        pieChartSliceFillStylePalette: seriesFillStylePalette,
        pieChartSliceStrokeStyle: uiBackgroundStrokeStyle,
        pieChartSliceLabelFont: fontOther,
        pieChartSliceLabelFillStyle: textFillStyle,
        pieChartConnectorStrokeStyle: uiBackgroundStrokeStyle,
        funnelChartBackgroundFillStyle: chartBackgroundFillStyle,
        funnelChartBackgroundStrokeStyle: lcjs.emptyLine,
        funnelChartTitleFont: fontChartTitles,
        funnelChartTitleFillStyle: textFillStyle,
        funnelChartSliceFillStylePalette: seriesFillStylePalette,
        funnelChartSliceStrokeStyle: uiBackgroundStrokeStyle,
        funnelChartSliceLabelFont: fontOther,
        funnelChartSliceLabelFillStyle: textFillStyle,
        funnelChartConnectorStrokeStyle: uiBackgroundStrokeStyle,
        pyramidChartBackgroundFillStyle: chartBackgroundFillStyle,
        pyramidChartBackgroundStrokeStyle: lcjs.emptyLine,
        pyramidChartTitleFont: fontChartTitles,
        pyramidChartTitleFillStyle: textFillStyle,
        pyramidChartSliceFillStylePalette: seriesFillStylePalette,
        pyramidChartSliceStrokeStyle: uiBackgroundStrokeStyle,
        pyramidChartSliceLabelFont: fontOther,
        pyramidChartSliceLabelFillStyle: textFillStyle,
        pyramidChartConnectorStrokeStyle: uiBackgroundStrokeStyle,
        gaugeChartBackgroundFillStyle: chartBackgroundFillStyle,
        gaugeChartBackgroundStrokeStyle: lcjs.emptyLine,
        gaugeChartTitleFont: fontChartTitles,
        gaugeChartTitleFillStyle: textFillStyle,
        gaugeChartEmptyGaugeFillStyle: isDark ? blackFillStyle : whiteFillStyle,
        gaugeChartEmptyGaugeStrokeStyle: uiBackgroundStrokeStyle,
        gaugeChartGaugeFillStyle: primaryDataFillStyle,
        gaugeChartIntervalLabelsFillStyle: textFillStyle,
        gaugeChartIntervalLabelsFont: fontOther,
        gaugeChartValueLabelFillStyle: textFillStyle,
        gaugeChartValueLabelFont: fontOther,
        uiPanelBackgroundFillStyle: chartBackgroundFillStyle,
        uiPanelBackgroundStrokeStyle: lcjs.emptyLine,
        onScreenMenuBackgroundColor: lcjs.ColorRGBA(254, 204, 0, 0.7),
        uiButtonFillStyle: uiButtonFillStyle,
        uiButtonStrokeStyle: uiBackgroundStrokeStyle,
        uiButtonSize: 10,
        uiBackgroundFillStyle: uiBackgroundFillStyle,
        uiBackgroundStrokeStyle: uiBackgroundStrokeStyle,
        uiTextFillStyle: textFillStyle,
        uiTextFont: fontOther,
        legendTitleFillStyle: textFillStyle,
        legendTitleFont: fontLegendTitle,
        cursorTickMarkerXBackgroundFillStyle: uiBackgroundFillStyle,
        cursorTickMarkerXBackgroundStrokeStyle: uiBackgroundStrokeStyle,
        cursorTickMarkerXTextFillStyle: textFillStyle,
        cursorTickMarkerXTextFont: fontOther,
        cursorTickMarkerYBackgroundFillStyle: uiBackgroundFillStyle,
        cursorTickMarkerYBackgroundStrokeStyle: uiBackgroundStrokeStyle,
        cursorTickMarkerYTextFillStyle: textFillStyle,
        cursorTickMarkerYTextFont: fontOther,
        cursorPointMarkerFillStyle: lcjs.emptyFill,
        cursorPointMarkerStrokeStyle: lcjs.emptyLine,
        cursorResultTableFillStyle: uiBackgroundFillStyle,
        cursorResultTableStrokeStyle: uiBackgroundStrokeStyle,
        cursorResultTableTextFillStyle: textFillStyle,
        cursorResultTableTextFont: fontOther,
        cursorGridStrokeStyleX: cursorGridStrokeStyle,
        cursorGridStrokeStyleY: cursorGridStrokeStyle,
        chartMarkerPointMarkerFillStyle: isDark ? whiteFillStyle : blackFillStyle,
        chartMarkerPointMarkerStrokeStyle: lcjs.emptyLine
      };
      return flatTheme;
    };

    /**
     * Adaptation of `Themes.darkGold` from `@arction/lcjs` using `makeFlatTheme` factory.
     *
     * ```ts
     *  // Example use
     *  import { flatThemeDark } from '@arction/lcjs-themes'
     *
     *  const chart = lightningChart().ChartXY({ theme: flatThemeDark })
     * ```
     * @public
     */
    var flatThemeDark = makeFlatTheme({
      isDark: true,
      fontFamily: 'Segoe UI, -apple-system, Verdana, Helvetica',
      backgroundColor: lcjs.ColorHEX('#181818ff'),
      textColor: lcjs.ColorHEX('#ffffc8ff'),
      dataColors: [lcjs.ColorHEX('#ffff5b'), lcjs.ColorHEX('#ffcd5b'), lcjs.ColorHEX('#ff9b5b'), lcjs.ColorHEX('#ffc4bc'), lcjs.ColorHEX('#ff94b8'), lcjs.ColorHEX('#db94c6'), lcjs.ColorHEX('#ebc4e0'), lcjs.ColorHEX('#a994c6'), lcjs.ColorHEX('#94e2c6'), lcjs.ColorHEX('#94ffb0'), lcjs.ColorHEX('#b4ffa5')],
      axisColor: lcjs.ColorHEX('#00000000'),
      gridLineColor: lcjs.ColorHEX('#303030ff'),
      uiBackgroundColor: lcjs.ColorHEX('#161616ff'),
      uiBorderColor: lcjs.ColorHEX('#ffffff'),
      dashboardSplitterColor: lcjs.ColorHEX('#2d2d2dff')
    });

    /**
     * Adaptation of `Themes.light` from `@arction/lcjs` using `makeFlatTheme` factory.
     *
     * ```ts
     *  // Example use
     *  import { flatThemeLight } from '@arction/lcjs-themes'
     *
     *  const chart = lightningChart().ChartXY({ theme: flatThemeLight })
     * ```
     * @public
     */
    var flatThemeLight = makeFlatTheme({
      isDark: false,
      fontFamily: 'Segoe UI, -apple-system, Verdana, Helvetica',
      backgroundColor: lcjs.ColorHEX('#ffffffff'),
      textColor: lcjs.ColorHEX('#212b31ff'),
      dataColors: [lcjs.ColorHEX('#1cb58c'), lcjs.ColorHEX('#ff8400'), lcjs.ColorHEX('#f02727'), lcjs.ColorHEX('#5679fb'), lcjs.ColorHEX('#02b5d5'), lcjs.ColorHEX('#0dd49e'), lcjs.ColorHEX('#16a703'), lcjs.ColorHEX('#ea67e8'), lcjs.ColorHEX('#3eb7b3'), lcjs.ColorHEX('#8c5d03'), lcjs.ColorHEX('#9b9eba')],
      axisColor: lcjs.ColorHEX('#00000000'),
      gridLineColor: lcjs.ColorHEX('#dcdcdcff'),
      uiBackgroundColor: lcjs.ColorHEX('#ffffffff'),
      uiBorderColor: lcjs.ColorHEX('#a8a8c7ff'),
      dashboardSplitterColor: lcjs.ColorHEX('#dbe3e9ff')
    });

    exports.flatThemeDark = flatThemeDark;
    exports.flatThemeLight = flatThemeLight;
    exports.makeFlatTheme = makeFlatTheme;

    Object.defineProperty(exports, '__esModule', { value: true });

    return exports;

})({}, lcjs);
