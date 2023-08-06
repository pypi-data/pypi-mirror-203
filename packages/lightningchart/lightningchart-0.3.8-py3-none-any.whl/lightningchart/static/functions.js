const functionLookup = {
    addArrayX: addArrayX,
    addArrayY: addArrayY,
    addArraysXY: addArraysXY,
    addAxis: addAxis,
    addBox2D: addBox2D,
    addChartMarkerXY: addChartMarkerXY,
    addData: addData,
    addIntensityValues: addIntensityValues,
    addOHLC: addOHLC,
    addValues: addValues,
    areaRangeSeries: areaRangeSeries,
    areaSeries: areaSeries,
    boxSeries2D: boxSeries2D,
    boxSeries3D: boxSeries3D,
    chart3D: chart3D,
    chartXY: chartXY,
    clearChart: clearChart,
    clearSeries: clearSeries,
    createChart3D: createChart3D,
    createChartXY: createChartXY,
    setAutoCursorMode: setAutoCursorMode,
    dashboard: dashboard,
    dispose: dispose,
    disposeDefaultAxis: disposeDefaultAxis,
    heatmapGridSeries: heatmapGridSeries,
    heatmapScrollingGridSeries: heatmapScrollingGridSeries,
    hideTitle: hideTitle,
    invalidateData: invalidateData,
    invalidateHeightMap: invalidateHeightMap,
    invalidateIntensityValues: invalidateIntensityValues,
    legend: legend,
    legendAdd: legendAdd,
    lineSeries2D: lineSeries2D,
    lineSeries3D: lineSeries3D,
    OHLCSeries: OHLCSeries,
    pointLineSeries2D: pointLineSeries2D,
    pointLineSeries3D: pointLineSeries3D,
    pointSeries2D: pointSeries2D,
    pointSeries3D: pointSeries3D,
    clearInstance: clearInstance,
    saveToFile: saveToFile,
    setAnimationZoom: setAnimationZoom,
    setAnimationsEnabled: setAnimationsEnabled,
    setAxisInterval: setAxisInterval,
    setBackgroundFillStyle: setBackgroundFillStyle,
    setBackgroundStrokeStyle: setBackgroundStrokeStyle,
    setBoundingBox: setBoundingBox,
    setBoundingBoxStrokeStyle: setBoundingBoxStrokeStyle,
    setColorShadingStyle: setColorShadingStyle,
    setCullMode: setCullMode,
    setCursorEnabled: setCursorEnabled,
    setDataCleaning: setDataCleaning,
    setDraggingMode: setDraggingMode,
    setEmptyFillStyle: setEmptyFillStyle,
    setHighFillStyle: setHighFillStyle,
    setHighlight: setHighlight,
    setGaugeHighlight: setGaugeHighlight,
    setIndividualPointRotationEnabled: setIndividualPointRotationEnabled,
    setIndividualPointSizeEnabled: setIndividualPointSizeEnabled,
    setIndividualPointValueEnabled: setIndividualPointValueEnabled,
    setIntensityInterpolation: setIntensityInterpolation,
    setLineFillStyle: setLineFillStyle,
    setLineThickness: setLineThickness,
    setLowFillStyle: setLowFillStyle,
    setMouseInteractions: setMouseInteractions,
    setPalettedFillStyle: setPalettedFillStyle,
    setPalettedPointFillStyle: setPalettedPointFillStyle,
    setPixelInterpolationMode: setPixelInterpolationMode,
    setPoint2DSize: setPoint2DSize,
    setPoint3DFillStyle: setPoint3DFillStyle,
    setPoint3DShape: setPoint3DShape,
    setPoint3DSize: setPoint3DSize,
    setPointFillStyle: setPointFillStyle,
    setPointMarkerVisibility: setPointMarkerVisibility,
    setPointRotation: setPointRotation,
    setPosition: setPosition,
    setScrollStrategy: setScrollStrategy,
    setSeriesBackgroundEffect: setSeriesBackgroundEffect,
    setSeriesBackgroundFillStyle: setSeriesBackgroundFillStyle,
    setSolidFillStyle: setSolidFillStyle,
    setText: setText,
    setTickStrategy: setTickStrategy,
    setTitle: setTitle,
    setTitleColor: setTitleColor,
    setTitleEffect: setTitleEffect,
    setTitleFont: setTitleFont,
    setTitleMargin: setTitleMargin,
    setTitlePosition: setTitlePosition,
    setTitleRotation: setTitleRotation,
    setVisible: setVisible,
    setVisibleAxis: setVisibleAxis,
    setWireframeStyle: setWireframeStyle,
    splineSeries: splineSeries,
    stepSeries: stepSeries,
    surfaceGridSeries: surfaceGridSeries,
    surfaceScrollingGridSeries: surfaceScrollingGridSeries,
    textBox: textBox,
    zoomBandChart: zoomBandChart,
    pieChart: pieChart,
    addSlice: addSlice,
    addSlices: addSlices,
    setLUT: setLUT,
    setLabelColor: setLabelColor,
    setLabelFont: setLabelFont,
    setInnerRadius: setInnerRadius,
    gaugeChart: gaugeChart,
    setAngleInterval: setAngleInterval,
    setGaugeInterval: setGaugeInterval,
    setGaugeValue: setGaugeValue,
    funnelChart: funnelChart,
    pyramidChart: pyramidChart,
    createPieChart: createPieChart,
    createGaugeChart: createGaugeChart,
    createFunnelChart: createFunnelChart,
    createPyramidChart: createPyramidChart,
    setGaugeColor: setGaugeColor,
    setDataLabelFillStyle: setDataLabelFillStyle,
    setDataLabelFont: setDataLabelFont,
    setThickness: setThickness,
    setFillStyle: setFillStyle,
    setHeadWidth: setHeadWidth,
    setNeckWidth: setNeckWidth,
    setSliceMode: setSliceMode,
    setSliceGap: setSliceGap,
    setSliceStrokeStyle: setSliceStrokeStyle,
    setGaugeStrokeStyle: setGaugeStrokeStyle,
    setLabelEffect: setLabelEffect,
    setSliceEffect: setSliceEffect,
    addDataXY: addDataXY,
    addDataXYZ: addDataXYZ,
}


function addDataXY(id, x, y, clear) {
    if (clear)
        objects[id].clear();

    const data = [];
    for (let i = 0; i < Math.min(x.length, y.length); i++) {
        data.push({
            x: x[i],
            y: y[i]
        });
    }
    objects[id].add(data);
}

function addDataXYZ(id, x, y, z, clear) {
    if (clear)
        objects[id].clear()

    const data = [];
    for (let i = 0; i < Math.min(x.length, y.length, z.length); i++) {
        data.push({
            x: x[i],
            y: y[i],
            z: z[i]
        });
    }
    objects[id].add(data);
}

function setSliceEffect(id, enabled) {
    objects[id].setSliceEffect(!!enabled);
}

function setLabelEffect(id, enabled) {
    objects[id].setLabelEffect(!!enabled);
}

function setGaugeStrokeStyle(id, thickness, color) {
    objects[id].setGaugeStrokeStyle(new lcjs.SolidLine({
        thickness: thickness,
        fillStyle: new lcjs.SolidFill({
            color: lcjs.ColorRGBA(color[0], color[1], color[2], color[3])
        })
    }));
}

function setSliceStrokeStyle(id, thickness, color) {
    objects[id].setSliceStrokeStyle(new lcjs.SolidLine({
        thickness: thickness,
        fillStyle: new lcjs.SolidFill({
            color: lcjs.ColorRGBA(color[0], color[1], color[2], color[3])
        })
    }));
}

function setSliceGap(id, gap) {
    objects[id].setSliceGap(gap);
}

function setSliceMode(id, mode) {
    objects[id].setSliceMode(mode);
}

function setNeckWidth(id, width) {
    objects[id].setNeckWidth(width);
}

function setHeadWidth(id, width) {
    objects[id].setHeadWidth(width);
}

function setFillStyle(id, color) {
    objects[id].getDefaultSlice().setFillStyle(
        new lcjs.SolidFill({color: lcjs.ColorRGBA(color[0], color[1], color[2], color[3])})
    );
}

function setThickness(id, thickness) {
    objects[id].setThickness(thickness);
}

function setDataLabelFont(id, size, family, weight, style) {
    objects[id].setDataLabelFont(new lcjs.FontSettings({
        size: size,
        family: family,
        weight: weight,
        style: style
    }));
}

function setDataLabelFillStyle(id, color) {
    objects[id].setDataLabelFillStyle(
        new lcjs.SolidFill({color: lcjs.ColorRGBA(color[0], color[1], color[2], color[3])})
    )
}

function setGaugeColor(id, color) {
    objects[id].setGaugeFillStyle(
        new lcjs.SolidFill({color: lcjs.ColorRGBA(color[0], color[1], color[2], color[3])})
    );
}

function createPyramidChart(id, dashboardID, column, row, colSpan, rowSpan) {
    objects[id] = objects[dashboardID].createPyramidChart({
        columnIndex: column,
        rowIndex: row,
        columnSpan: colSpan,
        rowSpan: rowSpan
    });
}

function createFunnelChart(id, dashboardID, column, row, colSpan, rowSpan) {
    objects[id] = objects[dashboardID].createFunnelChart({
        columnIndex: column,
        rowIndex: row,
        columnSpan: colSpan,
        rowSpan: rowSpan
    });
}

function createGaugeChart(id, dashboardID, column, row, colSpan, rowSpan) {
    objects[id] = objects[dashboardID].createGaugeChart({
        columnIndex: column,
        rowIndex: row,
        columnSpan: colSpan,
        rowSpan: rowSpan
    });
}

function createPieChart(id, dashboardID, column, row, colSpan, rowSpan) {
    objects[id] = objects[dashboardID].createPieChart({
        columnIndex: column,
        rowIndex: row,
        columnSpan: colSpan,
        rowSpan: rowSpan
    });
}

function pyramidChart(id, theme) {
    theme = getTheme(theme);
    objects[id] = lightningChart().Pyramid({theme: theme});
}

function funnelChart(id, theme) {
    theme = getTheme(theme);
    objects[id] = lightningChart().Funnel({theme: theme});
}

function setGaugeValue(id, value) {
    objects[id].getDefaultSlice().setValue(value);
}

function setGaugeInterval(id, start, end) {
    objects[id].getDefaultSlice().setInterval(start, end);
}

function setAngleInterval(id, start, end) {
    objects[id].setAngleInterval(start, end);
}

function gaugeChart(id, theme) {
    theme = getTheme(theme);
    objects[id] = lightningChart().Gauge({
        theme: theme,
        type: lcjs.GaugeChartTypes.Solid
    });
}

function setInnerRadius(id, radius) {
    objects[id].setInnerRadius(radius);
}

function setLabelFont(id, size, family, weight, style) {
    objects[id].setLabelFont(new lcjs.FontSettings({
        size: size,
        family: family,
        weight: weight,
        style: style
    }));
}

function setLabelColor(id, rgba) {
    objects[id].setLabelFillStyle(new lcjs.SolidFill({
        color: lcjs.ColorRGBA(rgba[0], rgba[1], rgba[2], rgba[3])
    }));
}

function setLUT(id, minValue, maxValue, minColor, maxColor, interpolate) {
    objects[id].setLUT(new lcjs.LUT({
        steps: [
            {value: minValue, color: lcjs.ColorRGBA(minColor[0], minColor[1], minColor[2], minColor[3])},
            {value: maxValue, color: lcjs.ColorRGBA(maxColor[0], maxColor[1], maxColor[2], maxColor[3])},
        ], interpolate: interpolate
    }));
}

function addSlices(id, slices) {
    objects[id].addSlices(slices);
}

function addSlice(id, name, value) {
    objects[id].addSlice(name, value);
}

function pieChart(id, theme, labelsInsideSlices) {
    theme = getTheme(theme);
    if (labelsInsideSlices) {
        objects[id] = lightningChart().Pie({
            theme: theme,
            type: lcjs.PieChartTypes.LabelsInsideSlices
        });
    } else {
        objects[id] = lightningChart().Pie({
            theme: theme,
            type: lcjs.PieChartTypes.LabelsOnSides
        });
    }
}

function getTheme(theme) {
    if (!theme)
        theme = ""
    switch (theme.toLowerCase()) {
        case 'light':
            return lcjs.Themes.light;
        case 'lightnature':
            return lcjs.Themes.lightNature;
        case 'cyberspace':
            return lcjs.Themes.cyberSpace;
        case 'turquoisehexagon':
            return lcjs.Themes.turquoiseHexagon;
        case 'flatdark':
            return lcjsThemes.flatThemeDark;
        case 'flatlight':
            return lcjsThemes.flatThemeLight;
        case 'darkgold':
            return lcjs.Themes.darkGold;
        default:
            const defaultTheme = lcjsThemes.makeFlatTheme({
                isDark: false,
                fontFamily: "Segoe UI, -apple-system, Verdana, Helvetica",
                backgroundColor: lcjs.ColorHEX("#faf0f0ff"),
                textColor: lcjs.ColorHEX("#000000ff"),
                dataColors: [
                    lcjs.ColorHEX("#0080c0"), lcjs.ColorHEX("#ff5050"), lcjs.ColorHEX("#7dff7d"),
                    lcjs.ColorHEX("#f0f000"), lcjs.ColorHEX("#fdaa11"), lcjs.ColorHEX("#60f9f9"),
                    lcjs.ColorHEX("#b45ad1"), lcjs.ColorHEX("#fa76d2")
                ],
                axisColor: lcjs.ColorHEX("#00000000"),
                gridLineColor: lcjs.ColorHEX("#c0c0c0ff"),
                uiBackgroundColor: lcjs.ColorHEX("#ffffffff"),
                uiBorderColor: lcjs.ColorHEX("#000000ff"),
                dashboardSplitterColor: lcjs.ColorHEX("#808080ff"),

            })
            return defaultTheme
    }
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function addArrayX(id, array) {
    objects[id].addArrayX(array);
}

function addArrayY(id, array) {
    objects[id].addArrayY(array);
}

function addArraysXY(id, arrayX, arrayY) {
    objects[id].addArraysXY(arrayX, arrayY);
}

function addAxis(id, chartID, axis, opposite, type, base) {
    if (axis === 'x') {
        objects[id] = objects[chartID].addAxisX({
            opposite: opposite,
            type: type,
            base: base
        });
    } else if (axis === 'y') {
        objects[id] = objects[chartID].addAxisY({
            opposite: opposite,
            type: type,
            base: base
        });
    }
}

function addBox2D(id, start, end, median, lowerQuartile, upperQuartile, lowerExtreme, upperExtreme) {
    objects[id].add({
        start: start,
        end: end,
        median: median,
        lowerQuartile: lowerQuartile,
        upperQuartile: upperQuartile,
        lowerExtreme: lowerExtreme,
        upperExtreme: upperExtreme
    });
}

function addChartMarkerXY(id, chartID) {
    objects[id] = objects[chartID].addChartMarkerXY();
}

function addData(id, data, clearPrevious) {
    if (clearPrevious)
        objects[id].clear();
    objects[id].add(data);
    /*
    try {
        const response = await fetch(`/fetch_protobuf?id=${room}&data_id=${dataID}`);
        const dataBytes = await response.arrayBuffer();
        const data = DataXY.decode(new Uint8Array(dataBytes));
        objects[id].add(data.points);
    } catch (error) {
        console.log(error);
    }
     */
}

function addIntensityValues(id, data) {
    objects[id].addIntensityValues(data);
}

function addOHLC(id, XOHLC) {
    objects[id].add(XOHLC);
}

function addValues(id, yValues, intensityValues) {
    objects[id].addValues({
        yValues: yValues,
        intensityValues: intensityValues
    });
}

function areaRangeSeries(id, chartID, xAxis, yAxis) {
    objects[id] = objects[chartID].addAreaRangeSeries({
        xAxis: objects[xAxis],
        yAxis: objects[yAxis]
    });
}

function areaSeries(id, chartID, xAxis, yAxis) {
    objects[id] = objects[chartID].addAreaSeries({
        xAxis: objects[xAxis],
        yAxis: objects[yAxis]
    });
}

function boxSeries2D(id, chartID, xAxis, yAxis) {
    objects[id] = objects[chartID].addBoxSeries({
        xAxis: objects[xAxis],
        yAxis: objects[yAxis]
    });
}

function boxSeries3D(id, chartID) {
    objects[id] = objects[chartID].addBoxSeries();
}

function chart3D(id, theme) {
    theme = getTheme(theme);
    objects[id] = lightningChart().Chart3D({theme: theme});
}

function chartXY(id, theme) {
    theme = getTheme(theme);
    objects[id] = lightningChart().ChartXY({theme: theme});
}

function clearChart(id) {
    if (objects[id]) {
        const seriesArray = objects[id].getSeries();
        Object.values(seriesArray).forEach(s => {
            s.dispose();
        });
    }
}

function clearSeries(id) {
    // BUG: browser view doesn't update until interaction
    if (objects[id])
        objects[id].clear();
}

function createChart3D(id, dashboardID, column, row, colSpan, rowSpan) {
    objects[id] = objects[dashboardID].createChart3D({
        columnIndex: column,
        rowIndex: row,
        columnSpan: colSpan,
        rowSpan: rowSpan
    });
}

function createChartXY(id, dashboardID, column, row, colSpan, rowSpan) {
    objects[id] = objects[dashboardID].createChartXY({
        columnIndex: column,
        rowIndex: row,
        columnSpan: colSpan,
        rowSpan: rowSpan
    });
}

function setAutoCursorMode(id, mode) {
    let cursorMode = lcjs.AutoCursorModes.snapToClosest;
    switch (mode.toLowerCase()) {
        case 'disabled':
            cursorMode = lcjs.AutoCursorModes.disabled;
            break;
        case 'onhover':
            cursorMode = lcjs.AutoCursorModes.onHover;
            break;
        case 'snaptoclosest':
            cursorMode = lcjs.AutoCursorModes.snapToClosest;
            break;
    }
    objects[id].setAutoCursorMode(cursorMode);
}

function dashboard(id, columns, rows, theme) {
    theme = getTheme(theme)
    objects[id] = lightningChart().Dashboard({
        numberOfColumns: columns,
        numberOfRows: rows,
        theme: theme
    });
}

function dispose(id) {
    objects[id].dispose();
    delete objects[id];
}

function disposeDefaultAxis(id, axis) {
    if (axis === 'x') {
        objects[id].getDefaultAxisX().dispose()
    } else if (axis === 'y') {
        objects[id].getDefaultAxisY().dispose()
    } else if (axis === 'z') {
        objects[id].getDefaultAxisZ().dispose()
    }
}

function heatmapGridSeries(id, chartID, columns, rows, start, end, step, dataOrder, xAxis, yAxis) {
    objects[id] = objects[chartID].addHeatmapGridSeries({
        columns: columns,
        rows: rows,
        start: {x: start[0], y: start[1]},
        end: (end ? {x: end[0], y: end[1]} : undefined),
        step: {x: step[0], y: step[1]},
        dataOrder: dataOrder,
        xAxis: objects[xAxis],
        yAxis: objects[yAxis]
    });
}

function heatmapScrollingGridSeries(id, chartID, scroll, resolution, start, step, xAxis, yAxis) {
    objects[id] = objects[chartID].addHeatmapScrollingGridSeries({
        scrollDimension: scroll,
        resolution: resolution,
        start: {x: start[0], y: start[1]},
        step: {x: step[0], y: step[1]},
        xAxis: objects[xAxis],
        yAxis: objects[yAxis]
    })
}

function hideTitle(id) {
    objects[id].setTitleFillStyle(lcjs.emptyFill);
}

function invalidateData(id, data) {
    objects[id].invalidateData(data);
}

function invalidateHeightMap(id, data, iColumn = undefined, iRow = undefined) {
    if (iColumn && iRow) {
        objects[id].invalidateHeightMap({
            iColumn: iColumn,
            iRow: iRow,
            values: data
        })
    } else {
        objects[id].invalidateHeightMap(data);
    }
}

function invalidateIntensityValues(id, data, iColumn = undefined, iRow = undefined) {
    if (iColumn && iRow) {
        objects[id].invalidateIntensityValues({
            iColumn: iColumn,
            iRow: iRow,
            values: data
        })
    } else {
        objects[id].invalidateIntensityValues(data);
    }
}

function legend(id, chartID, horizontal) {
    if (horizontal)
        objects[id] = objects[chartID].addLegendBox(lcjs.LegendBoxBuilders.HorizontalLegendBox)
    else
        objects[id] = objects[chartID].addLegendBox()
}

function legendAdd(id, chartID) {
    objects[id].add(objects[chartID])
}

function lineSeries2D(id, chartID, pattern, xAxis, yAxis, individualLookupValuesEnabled) {
    objects[id] = objects[chartID].addLineSeries({
        dataPattern: {pattern: pattern},
        individualLookupValuesEnabled: individualLookupValuesEnabled,
        xAxis: objects[xAxis],
        yAxis: objects[yAxis]
    });
}

function lineSeries3D(id, chartID) {
    objects[id] = objects[chartID].addLineSeries();
}

function OHLCSeries(id, chartID, xAxis, yAxis) {
    objects[id] = objects[chartID].addOHLCSeries({
        xAxis: objects[xAxis],
        yAxis: objects[yAxis]
    });
}

function pointLineSeries2D(id, chartID, pattern, shape, xAxis, yAxis) {
    objects[id] = objects[chartID].addPointLineSeries({
        dataPattern: {pattern: pattern},
        pointShape: shape,
        xAxis: objects[xAxis],
        yAxis: objects[yAxis]
    });
}

function pointLineSeries3D(id, chartID, individualLookupValuesEnabled, individualPointColorEnabled,
                           individualPointSizeAxisEnabled, individualPointSizeEnabled, pointCloudSeries) {
    if (!!pointCloudSeries === true)
        pointCloudSeries = lcjs.PointSeriesTypes3D.Pixelated;
    else
        pointCloudSeries = lcjs.PointSeriesTypes3D.Triangulated;
    objects[id] = objects[chartID].addPointLineSeries({
        individualLookupValuesEnabled: individualLookupValuesEnabled,
        individualPointColorEnabled: individualPointColorEnabled,
        individualPointSizeAxisEnabled: individualPointSizeAxisEnabled,
        individualPointSizeEnabled: individualPointSizeEnabled,
        type: pointCloudSeries
    });
}

function pointSeries2D(id, chartID, shape, xAxis, yAxis) {
    objects[id] = objects[chartID].addPointSeries({
        pointShape: shape,
        xAxis: objects[xAxis],
        yAxis: objects[yAxis]
    });
}

function pointSeries3D(id, chartID, individualLookupValuesEnabled, individualPointColorEnabled,
                       individualPointSizeAxisEnabled, individualPointSizeEnabled, pointCloudSeries) {
    if (!!pointCloudSeries === true)
        pointCloudSeries = lcjs.PointSeriesTypes3D.Pixelated;
    else
        pointCloudSeries = lcjs.PointSeriesTypes3D.Triangulated;
    objects[id] = objects[chartID].addPointSeries({
        individualLookupValuesEnabled: individualLookupValuesEnabled,
        individualPointColorEnabled: individualPointColorEnabled,
        individualPointSizeAxisEnabled: individualPointSizeAxisEnabled,
        individualPointSizeEnabled: individualPointSizeEnabled,
        type: pointCloudSeries
    });
}


function clearInstance(id) {
    for (const o in objects) {
        objects[o].dispose();
        delete objects[o];
    }
}

async function saveToFile(id, fileName, type, encoderOptions) {
    await sleep(1000); // sleep for 1s if render isn't finished
    objects[id].saveToFile(fileName, type, encoderOptions);
}

function setAnimationZoom(id, enabled) {
    objects[id].setAnimationZoom(!!enabled);
}

function setAnimationsEnabled(id, enabled) {
    objects[id].setAnimationsEnabled(!!enabled);
}

function setAxisInterval(id, start, end, axis, stop, animate) {

    const parameters = {
        start: start,
        end: end,
        stopAxisAfter: !!stop,
        animate: animate
    }

    if (axis === 'x') {
        objects[id].getDefaultAxisX().setInterval(parameters);
    } else if (axis === 'y') {
        objects[id].getDefaultAxisY().setInterval(parameters);
    } else if (axis === 'z') {
        objects[id].getDefaultAxisZ().setInterval(parameters);
    } else {
        objects[axis].setInterval(parameters);
    }
}

function setBackgroundFillStyle(id, color) {
    objects[id].setBackgroundFillStyle(new lcjs.SolidFill({
        color: lcjs.ColorRGBA(color[0], color[1], color[2], color[3])
    }));
}

function setBackgroundStrokeStyle(id, thickness, color) {
    objects[id].setBackgroundStrokeStyle(new lcjs.SolidLine({
        thickness: thickness,
        fillStyle: new lcjs.SolidFill({
            color: lcjs.ColorRGBA(color[0], color[1], color[2], color[3])
        })
    }));
}

function setBoundingBox(id, x, y, z) {
    objects[id].setBoundingBox({
        x: x, y: y, z: z
    });
}

function setBoundingBoxStrokeStyle(id, thickness, color) {
    objects[id].setBoundingBoxStrokeStyle(new lcjs.SolidLine({
        fillStyle: new lcjs.SolidFill({
            color: lcjs.ColorRGBA(color[0], color[1], color[2], color[3])
        }),
        thickness: thickness
    }));
}

function setColorShadingStyle(id, style, specularReflection, specularColor) {
    if (style === 'phong') {
        objects[id].setColorShadingStyle(new lcjs.ColorShadingStyles.Phong({
            specularReflection: specularReflection,
            specularColor: lcjs.ColorRGBA(specularColor[0], specularColor[1], specularColor[2], specularColor[3])
        }))
    } else {
        objects[id].setColorShadingStyle(new lcjs.ColorShadingStyles.Simple())
    }
}

function setCullMode(id, mode) {
    objects[id].setCullMode(mode);
}

function setCursorEnabled(id, enabled) {
    objects[id].setCursorEnabled(!!enabled);
}

function setDataCleaning(id, enabled) {
    if (!!enabled)
        objects[id].setDataCleaning({minDataPointCount: 1});
    else
        objects[id].setDataCleaning(undefined);
}

function setDraggingMode(id, mode) {
    switch (mode.toLowerCase()) {
        case 'notdraggable':
            mode = 0;
            break;
        case 'onlyhorizontal':
            mode = 2;
            break;
        case 'onlyvertical':
            mode = 3;
            break;
        default:
            mode = 1;
    }
    objects[id].setDraggingMode(mode);
}

function setEmptyFillStyle(id, color) {
    objects[id]
        .setFillStyle(lcjs.emptyFill)
        .setWireframeStyle(new lcjs.SolidFill({color: lcjs.ColorRGBA(color[0], color[1], color[2], color[3])}))
}

function setHighFillStyle(id, color) {
    objects[id].setHighFillStyle(new lcjs.SolidFill({
        color: lcjs.ColorRGBA(color[0], color[1], color[2], color[3])
    }))
}

function setHighlight(id, highlight) {
    objects[id].setHighlight(highlight);
}

function setGaugeHighlight(id, highlight) {
    objects[id].getDefaultSlice().setHighlight(highlight);
}

function setIndividualPointRotationEnabled(id, enabled) {
    objects[id].setIndividualPointRotationEnabled(!!enabled);
}

function setIndividualPointSizeEnabled(id, enabled) {
    objects[id].setIndividualPointSizeEnabled(!!enabled);
}

function setIndividualPointValueEnabled(id, enabled) {
    objects[id].setIndividualPointValueEnabled(!!enabled);
}

function setIntensityInterpolation(id, interpolation) {
    if (interpolation === 'bilinear')
        objects[id].setIntensityInterpolation('bilinear');
    else
        objects[id].setIntensityInterpolation('disabled');
}

function setLineFillStyle(id, color) {
    objects[id].setStrokeStyle(new lcjs.SolidLine({
        thickness: 1,
        fillStyle: new lcjs.SolidFill({
            color: lcjs.ColorRGBA(color[0], color[1], color[2], color[3])
        })
    }))
}

function setLineThickness(id, width) {
    objects[id].setStrokeStyle((stroke) => stroke.setThickness(width))
}

function setLowFillStyle(id, color) {
    objects[id].setLowFillStyle(new lcjs.SolidFill({
        color: lcjs.ColorRGBA(color[0], color[1], color[2], color[3])
    }))
}

function setMouseInteractions(id, bool) {
    objects[id].setMouseInteractions(!!bool);
}

function setPalettedFillStyle(id, minValue, maxValue, minColor, maxColor, lookUpProperty) {
    objects[id].setFillStyle(new lcjs.PalettedFill({
        lookUpProperty: lookUpProperty,
        lut: new lcjs.LUT({
            interpolate: true,
            steps: [
                {value: minValue, color: lcjs.ColorRGBA(minColor[0], minColor[1], minColor[2], minColor[3])},
                {value: maxValue, color: lcjs.ColorRGBA(maxColor[0], maxColor[1], maxColor[2], minColor[3])}
            ]
        })
    }));
}

function setPalettedPointFillStyle(id, minValue, maxValue, minColor, maxColor, lookUpProperty) {
    objects[id].setPointFillStyle(new lcjs.PalettedFill({
        lookUpProperty: lookUpProperty,
        lut: new lcjs.LUT({
            interpolate: true,
            steps: [
                {value: minValue, color: lcjs.ColorRGBA(minColor[0], minColor[1], minColor[2], minColor[3])},
                {value: maxValue, color: lcjs.ColorRGBA(maxColor[0], maxColor[1], maxColor[2], maxColor[3])},
            ]
        })
    }))
}

function setPixelInterpolationMode(id, interpolation) {
    if (interpolation === 'bilinear')
        objects[id].setPixelInterpolationMode('bilinear');
    else
        objects[id].setPixelInterpolationMode('disabled');
}

function setPoint2DSize(id, size) {
    objects[id].setPointSize(size);
}

function setPoint3DFillStyle(id, color) {
    objects[id].setPointStyle((pointStyle) => pointStyle
        .setFillStyle(new lcjs.SolidFill({
            color: lcjs.ColorRGBA(color[0], color[1], color[2], color[3])
        }))
    )
}

function setPoint3DShape(id, shape) {
    objects[id].setPointStyle((pointStyle) => pointStyle
        .setShape(shape)
    )
}

function setPoint3DSize(id, size) {
    objects[id].setPointStyle((pointStyle) => pointStyle
        .setSize(size)
    )
}

function setPointFillStyle(id, color) {
    objects[id].setPointFillStyle(new lcjs.SolidFill({
        color: lcjs.ColorRGBA(color[0], color[1], color[2], color[3])
    }))
}

function setPointMarkerVisibility(id, visibility) {
    switch (visibility.toLowerCase()) {
        case 'never':
            visibility = 0;
            break
        case 'whendragged':
            visibility = 3;
            break;
        case 'whenhovered':
            visibility = 2;
            break;
        case 'whenhoveredordragged':
            visibility = 5;
            break;
        case 'whennotdragged':
            visibility = 4;
            break;
        default:
            visibility = 1;
    }
    objects[id].setPointMarkerVisibility(visibility);
}


function setPointRotation(id, angle) {
    objects[id].setPointRotation(angle);
}

function setPosition(id, x, y) {
    objects[id].setPosition({x: x, y: y})
}

function setScrollStrategy(id, strategy, axis) {
    switch (strategy) {
        case 'expansion':
            strategy = lcjs.AxisScrollStrategies.expansion;
            break;
        case 'fitting':
            strategy = lcjs.AxisScrollStrategies.fitting;
            break;
        case 'regressive':
            strategy = lcjs.AxisScrollStrategies.regressive;
            break;
        default:
            strategy = lcjs.AxisScrollStrategies.progressive;
    }
    if (axis === 'x') {
        objects[id].getDefaultAxisX().setScrollStrategy(strategy);
    } else if (axis === 'y') {
        objects[id].getDefaultAxisY().setScrollStrategy(strategy);
    } else if (axis === 'z') {
        objects[id].getDefaultAxisZ().setScrollStrategy(strategy);
    } else {
        objects[axis].setScrollStrategy(strategy);
    }
}

function setSeriesBackgroundEffect(id, enabled) {
    objects[id].setSeriesBackgroundEffect(enabled);
}

function setSeriesBackgroundFillStyle(id, color) {
    objects[id].setSeriesBackgroundFillStyle(new lcjs.SolidFill({
        color: lcjs.ColorRGBA(color[0], color[1], color[2], color[3])
    }));
}

function setSolidFillStyle(id, color) {
    objects[id].setFillStyle(new lcjs.SolidFill({color: lcjs.ColorRGBA(color[0], color[1], color[2], color[3])}))
}

function setText(id, text) {
    objects[id].setText(text)
}

function setTickStrategy(id, strategy, axis, timeOrigin) {
    if (timeOrigin) {
        const date = new Date(timeOrigin * 1000);
        timeOrigin = (tickStrategy) => tickStrategy.setDateOrigin(date);
    } else
        timeOrigin = null;

    if (axis === 'x') {
        objects[id].getDefaultAxisX().setTickStrategy(strategy, timeOrigin);
    } else if (axis === 'y') {
        objects[id].getDefaultAxisY().setTickStrategy(strategy, timeOrigin);
    } else if (axis === 'z') {
        objects[id].getDefaultAxisZ().setTickStrategy(strategy, timeOrigin);
    } else {
        objects[axis].setTickStrategy(strategy, timeOrigin);
    }
}

function setTitle(id, title) {
    if (objects[id])
        objects[id].setTitle(title);
}

function setTitleColor(id, color) {
    objects[id].setTitleFillStyle(new lcjs.SolidFill({
        color: lcjs.ColorRGBA(color[0], color[1], color[2], color[3])
    }));
}

function setTitleEffect(id, enabled) {
    objects[id].setTitleEffect(enabled);
}

function setTitleFont(id, size, style) {
    objects[id].setTitleFont(new lcjs.FontSettings({
        size: size,
        style: style
    }));
}

function setTitleMargin(id, margin) {
    objects[id].setTitleMargin(margin);
}

function setTitlePosition(id, position) {
    objects[id].setTitlePosition(position);
}

function setTitleRotation(id, value) {
    objects[id].setTitleRotation(value);
}

function setVisible(id, visible) {
    objects[id].setVisible(!!visible);
}

function setVisibleAxis(id, axis, visible) {
    if (axis === 'x') {
        objects[id].getDefaultAxisX().setVisible(!!visible);
    } else if (axis === 'y') {
        objects[id].getDefaultAxisY().setVisible(!!visible);
    } else if (axis === 'z') {
        objects[id].getDefaultAxisZ().setVisible(!!visible);
    } else {
        objects[axis].setVisible(!!visible);
    }

}

function setWireframeStyle(id, style, color) {
    if (style !== 'empty' && color) {
        objects[id].setWireframeStyle(new lcjs.SolidLine({
            thickness: 1,
            fillStyle: new lcjs.SolidFill({
                color: lcjs.ColorRGBA(color[0], color[1], color[2], color[3])
            })
        }));
    } else {
        objects[id].setWireframeStyle(lcjs.emptyLine);
    }
}

function splineSeries(id, chartID, pattern, shape, xAxis, yAxis) {
    objects[id] = objects[chartID].addSplineSeries({
        dataPattern: {pattern: pattern},
        pointShape: shape,
        xAxis: objects[xAxis],
        yAxis: objects[yAxis]
    })
}

function stepSeries(id, chartID, pattern, mode, shape, xAxis, yAxis) {
    objects[id] = objects[chartID].addStepSeries({
        dataPattern: {pattern: pattern},
        mode: mode,
        pointShape: shape,
        xAxis: objects[xAxis],
        yAxis: objects[yAxis]
    });
}

function surfaceGridSeries(id, chart, columns, rows, dataOrder, start, end, step) {
    objects[id] = objects[chart].addSurfaceGridSeries({
        columns: columns,
        rows: rows,
        dataOrder: dataOrder,
        start: {x: start[0], z: start[1]},
        end: (end ? {x: end[0], z: end[1]} : undefined),
        step: {x: step[0], z: step[1]}
    });
}

function surfaceScrollingGridSeries(id, chartID, columns, rows, scroll, start, step) {
    objects[id] = objects[chartID].addSurfaceScrollingGridSeries({
        columns: columns,
        rows: rows,
        scrollDimension: scroll,
        start: {x: start[0], z: start[1]},
        step: {x: step[0], z: step[1]}
    });
}

function textBox(id, chartID) {
    objects[id] = objects[chartID].addUIElement().setText('').addElement(lcjs.UIElementBuilders.TextBox)
}

function zoomBandChart(id, dashboardID, chartID, columnIndex, columnSpan, rowIndex, rowSpan, axis) {
    objects[id] = objects[dashboardID].createZoomBandChart({
        columnIndex: columnIndex,
        columnSpan: columnSpan,
        rowIndex: rowIndex,
        rowSpan: rowSpan,
        axis: (axis === 'x'
            ? objects[chartID].getDefaultAxisX()
            : (axis === 'y'
                ? objects[chartID].getDefaultAxisY()
                : objects[axis]))
    });
}
