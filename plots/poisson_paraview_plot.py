import sys
import os.path

pvd_input = os.path.join(os.path.dirname(__file__), "..", "computation", "poisson.pvd" )
png_output = os.path.join(os.path.dirname(__file__), "poisson_field.png" )

#### import the simple module from the paraview
from paraview.simple import *

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'PVD Reader'
poissonpvd = PVDReader(FileName=str(pvd_input))

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1564, 741]

# get color transfer function/color map for 'f_253'
f_253LUT = GetColorTransferFunction('f_253')

# get opacity transfer function/opacity map for 'f_253'
f_253PWF = GetOpacityTransferFunction('f_253')

# show data in view
poissonpvdDisplay = Show(poissonpvd, renderView1)
# trace defaults for the display properties.
poissonpvdDisplay.Representation = 'Surface'
poissonpvdDisplay.AmbientColor = [1.0, 1.0, 1.0]
poissonpvdDisplay.ColorArrayName = ['POINTS', 'f_253']
poissonpvdDisplay.DiffuseColor = [1.0, 1.0, 1.0]
poissonpvdDisplay.LookupTable = f_253LUT
poissonpvdDisplay.MapScalars = 1
poissonpvdDisplay.InterpolateScalarsBeforeMapping = 1
poissonpvdDisplay.Opacity = 1.0
poissonpvdDisplay.PointSize = 2.0
poissonpvdDisplay.LineWidth = 1.0
poissonpvdDisplay.Interpolation = 'Gouraud'
poissonpvdDisplay.Specular = 0.0
poissonpvdDisplay.SpecularColor = [1.0, 1.0, 1.0]
poissonpvdDisplay.SpecularPower = 100.0
poissonpvdDisplay.Ambient = 0.0
poissonpvdDisplay.Diffuse = 1.0
poissonpvdDisplay.EdgeColor = [0.0, 0.0, 0.5]
poissonpvdDisplay.BackfaceRepresentation = 'Follow Frontface'
poissonpvdDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
poissonpvdDisplay.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
poissonpvdDisplay.BackfaceOpacity = 1.0
poissonpvdDisplay.Position = [0.0, 0.0, 0.0]
poissonpvdDisplay.Scale = [1.0, 1.0, 1.0]
poissonpvdDisplay.Orientation = [0.0, 0.0, 0.0]
poissonpvdDisplay.Origin = [0.0, 0.0, 0.0]
poissonpvdDisplay.Pickable = 1
poissonpvdDisplay.Texture = None
poissonpvdDisplay.Triangulate = 0
poissonpvdDisplay.NonlinearSubdivisionLevel = 1
poissonpvdDisplay.UseDataPartitions = 0
poissonpvdDisplay.OSPRayUseScaleArray = 0
poissonpvdDisplay.OSPRayScaleArray = 'f_253'
poissonpvdDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
poissonpvdDisplay.Orient = 0
poissonpvdDisplay.OrientationMode = 'Direction'
poissonpvdDisplay.SelectOrientationVectors = 'None'
poissonpvdDisplay.Scaling = 0
poissonpvdDisplay.ScaleMode = 'No Data Scaling Off'
poissonpvdDisplay.ScaleFactor = 0.1
poissonpvdDisplay.SelectScaleArray = 'f_253'
poissonpvdDisplay.GlyphType = 'Arrow'
poissonpvdDisplay.UseGlyphTable = 0
poissonpvdDisplay.GlyphTableIndexArray = 'f_253'
poissonpvdDisplay.UseCompositeGlyphTable = 0
poissonpvdDisplay.DataAxesGrid = 'GridAxesRepresentation'
poissonpvdDisplay.SelectionCellLabelBold = 0
poissonpvdDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
poissonpvdDisplay.SelectionCellLabelFontFamily = 'Arial'
poissonpvdDisplay.SelectionCellLabelFontSize = 18
poissonpvdDisplay.SelectionCellLabelItalic = 0
poissonpvdDisplay.SelectionCellLabelJustification = 'Left'
poissonpvdDisplay.SelectionCellLabelOpacity = 1.0
poissonpvdDisplay.SelectionCellLabelShadow = 0
poissonpvdDisplay.SelectionPointLabelBold = 0
poissonpvdDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
poissonpvdDisplay.SelectionPointLabelFontFamily = 'Arial'
poissonpvdDisplay.SelectionPointLabelFontSize = 18
poissonpvdDisplay.SelectionPointLabelItalic = 0
poissonpvdDisplay.SelectionPointLabelJustification = 'Left'
poissonpvdDisplay.SelectionPointLabelOpacity = 1.0
poissonpvdDisplay.SelectionPointLabelShadow = 0
poissonpvdDisplay.PolarAxes = 'PolarAxesRepresentation'
poissonpvdDisplay.ScalarOpacityFunction = f_253PWF
poissonpvdDisplay.ScalarOpacityUnitDistance = 0.04419417382415923
poissonpvdDisplay.SelectMapper = 'Projected tetra'
poissonpvdDisplay.SamplingDimensions = [128, 128, 128]
poissonpvdDisplay.UseFloatingPointFrameBuffer = 1
poissonpvdDisplay.GaussianRadius = 0.05
poissonpvdDisplay.ShaderPreset = 'Sphere'
poissonpvdDisplay.Emissive = 0
poissonpvdDisplay.ScaleByArray = 0
poissonpvdDisplay.SetScaleArray = ['POINTS', 'f_253']
poissonpvdDisplay.ScaleTransferFunction = 'PiecewiseFunction'
poissonpvdDisplay.OpacityByArray = 0
poissonpvdDisplay.OpacityArray = ['POINTS', 'f_253']
poissonpvdDisplay.OpacityTransferFunction = 'PiecewiseFunction'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
poissonpvdDisplay.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'Arrow' selected for 'GlyphType'
poissonpvdDisplay.GlyphType.TipResolution = 6
poissonpvdDisplay.GlyphType.TipRadius = 0.1
poissonpvdDisplay.GlyphType.TipLength = 0.35
poissonpvdDisplay.GlyphType.ShaftResolution = 6
poissonpvdDisplay.GlyphType.ShaftRadius = 0.03
poissonpvdDisplay.GlyphType.Invert = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
poissonpvdDisplay.DataAxesGrid.XTitle = 'X Axis'
poissonpvdDisplay.DataAxesGrid.YTitle = 'Y Axis'
poissonpvdDisplay.DataAxesGrid.ZTitle = 'Z Axis'
poissonpvdDisplay.DataAxesGrid.XTitleColor = [1.0, 1.0, 1.0]
poissonpvdDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
poissonpvdDisplay.DataAxesGrid.XTitleBold = 0
poissonpvdDisplay.DataAxesGrid.XTitleItalic = 0
poissonpvdDisplay.DataAxesGrid.XTitleFontSize = 12
poissonpvdDisplay.DataAxesGrid.XTitleShadow = 0
poissonpvdDisplay.DataAxesGrid.XTitleOpacity = 1.0
poissonpvdDisplay.DataAxesGrid.YTitleColor = [1.0, 1.0, 1.0]
poissonpvdDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
poissonpvdDisplay.DataAxesGrid.YTitleBold = 0
poissonpvdDisplay.DataAxesGrid.YTitleItalic = 0
poissonpvdDisplay.DataAxesGrid.YTitleFontSize = 12
poissonpvdDisplay.DataAxesGrid.YTitleShadow = 0
poissonpvdDisplay.DataAxesGrid.YTitleOpacity = 1.0
poissonpvdDisplay.DataAxesGrid.ZTitleColor = [1.0, 1.0, 1.0]
poissonpvdDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
poissonpvdDisplay.DataAxesGrid.ZTitleBold = 0
poissonpvdDisplay.DataAxesGrid.ZTitleItalic = 0
poissonpvdDisplay.DataAxesGrid.ZTitleFontSize = 12
poissonpvdDisplay.DataAxesGrid.ZTitleShadow = 0
poissonpvdDisplay.DataAxesGrid.ZTitleOpacity = 1.0
poissonpvdDisplay.DataAxesGrid.FacesToRender = 63
poissonpvdDisplay.DataAxesGrid.CullBackface = 0
poissonpvdDisplay.DataAxesGrid.CullFrontface = 1
poissonpvdDisplay.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
poissonpvdDisplay.DataAxesGrid.ShowGrid = 0
poissonpvdDisplay.DataAxesGrid.ShowEdges = 1
poissonpvdDisplay.DataAxesGrid.ShowTicks = 1
poissonpvdDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
poissonpvdDisplay.DataAxesGrid.AxesToLabel = 63
poissonpvdDisplay.DataAxesGrid.XLabelColor = [1.0, 1.0, 1.0]
poissonpvdDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
poissonpvdDisplay.DataAxesGrid.XLabelBold = 0
poissonpvdDisplay.DataAxesGrid.XLabelItalic = 0
poissonpvdDisplay.DataAxesGrid.XLabelFontSize = 12
poissonpvdDisplay.DataAxesGrid.XLabelShadow = 0
poissonpvdDisplay.DataAxesGrid.XLabelOpacity = 1.0
poissonpvdDisplay.DataAxesGrid.YLabelColor = [1.0, 1.0, 1.0]
poissonpvdDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
poissonpvdDisplay.DataAxesGrid.YLabelBold = 0
poissonpvdDisplay.DataAxesGrid.YLabelItalic = 0
poissonpvdDisplay.DataAxesGrid.YLabelFontSize = 12
poissonpvdDisplay.DataAxesGrid.YLabelShadow = 0
poissonpvdDisplay.DataAxesGrid.YLabelOpacity = 1.0
poissonpvdDisplay.DataAxesGrid.ZLabelColor = [1.0, 1.0, 1.0]
poissonpvdDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
poissonpvdDisplay.DataAxesGrid.ZLabelBold = 0
poissonpvdDisplay.DataAxesGrid.ZLabelItalic = 0
poissonpvdDisplay.DataAxesGrid.ZLabelFontSize = 12
poissonpvdDisplay.DataAxesGrid.ZLabelShadow = 0
poissonpvdDisplay.DataAxesGrid.ZLabelOpacity = 1.0
poissonpvdDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
poissonpvdDisplay.DataAxesGrid.XAxisPrecision = 2
poissonpvdDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
poissonpvdDisplay.DataAxesGrid.XAxisLabels = []
poissonpvdDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
poissonpvdDisplay.DataAxesGrid.YAxisPrecision = 2
poissonpvdDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
poissonpvdDisplay.DataAxesGrid.YAxisLabels = []
poissonpvdDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
poissonpvdDisplay.DataAxesGrid.ZAxisPrecision = 2
poissonpvdDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
poissonpvdDisplay.DataAxesGrid.ZAxisLabels = []

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
poissonpvdDisplay.PolarAxes.Visibility = 0
poissonpvdDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
poissonpvdDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
poissonpvdDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
poissonpvdDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
poissonpvdDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
poissonpvdDisplay.PolarAxes.EnableCustomRange = 0
poissonpvdDisplay.PolarAxes.CustomRange = [0.0, 1.0]
poissonpvdDisplay.PolarAxes.PolarAxisVisibility = 1
poissonpvdDisplay.PolarAxes.RadialAxesVisibility = 1
poissonpvdDisplay.PolarAxes.DrawRadialGridlines = 1
poissonpvdDisplay.PolarAxes.PolarArcsVisibility = 1
poissonpvdDisplay.PolarAxes.DrawPolarArcsGridlines = 1
poissonpvdDisplay.PolarAxes.NumberOfRadialAxes = 0
poissonpvdDisplay.PolarAxes.AutoSubdividePolarAxis = 1
poissonpvdDisplay.PolarAxes.NumberOfPolarAxis = 0
poissonpvdDisplay.PolarAxes.MinimumRadius = 0.0
poissonpvdDisplay.PolarAxes.MinimumAngle = 0.0
poissonpvdDisplay.PolarAxes.MaximumAngle = 90.0
poissonpvdDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
poissonpvdDisplay.PolarAxes.Ratio = 1.0
poissonpvdDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
poissonpvdDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
poissonpvdDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
poissonpvdDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
poissonpvdDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
poissonpvdDisplay.PolarAxes.PolarAxisTitleVisibility = 1
poissonpvdDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
poissonpvdDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
poissonpvdDisplay.PolarAxes.PolarLabelVisibility = 1
poissonpvdDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
poissonpvdDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
poissonpvdDisplay.PolarAxes.RadialLabelVisibility = 1
poissonpvdDisplay.PolarAxes.RadialLabelFormat = '%-#3.1f'
poissonpvdDisplay.PolarAxes.RadialLabelLocation = 'Bottom'
poissonpvdDisplay.PolarAxes.RadialUnitsVisibility = 1
poissonpvdDisplay.PolarAxes.ScreenSize = 10.0
poissonpvdDisplay.PolarAxes.PolarAxisTitleColor = [1.0, 1.0, 1.0]
poissonpvdDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
poissonpvdDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
poissonpvdDisplay.PolarAxes.PolarAxisTitleBold = 0
poissonpvdDisplay.PolarAxes.PolarAxisTitleItalic = 0
poissonpvdDisplay.PolarAxes.PolarAxisTitleShadow = 0
poissonpvdDisplay.PolarAxes.PolarAxisTitleFontSize = 12
poissonpvdDisplay.PolarAxes.PolarAxisLabelColor = [1.0, 1.0, 1.0]
poissonpvdDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
poissonpvdDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
poissonpvdDisplay.PolarAxes.PolarAxisLabelBold = 0
poissonpvdDisplay.PolarAxes.PolarAxisLabelItalic = 0
poissonpvdDisplay.PolarAxes.PolarAxisLabelShadow = 0
poissonpvdDisplay.PolarAxes.PolarAxisLabelFontSize = 12
poissonpvdDisplay.PolarAxes.LastRadialAxisTextColor = [1.0, 1.0, 1.0]
poissonpvdDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
poissonpvdDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
poissonpvdDisplay.PolarAxes.LastRadialAxisTextBold = 0
poissonpvdDisplay.PolarAxes.LastRadialAxisTextItalic = 0
poissonpvdDisplay.PolarAxes.LastRadialAxisTextShadow = 0
poissonpvdDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
poissonpvdDisplay.PolarAxes.SecondaryRadialAxesTextColor = [1.0, 1.0, 1.0]
poissonpvdDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
poissonpvdDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
poissonpvdDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
poissonpvdDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
poissonpvdDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
poissonpvdDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
poissonpvdDisplay.PolarAxes.EnableDistanceLOD = 1
poissonpvdDisplay.PolarAxes.DistanceLODThreshold = 0.7
poissonpvdDisplay.PolarAxes.EnableViewAngleLOD = 1
poissonpvdDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
poissonpvdDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
poissonpvdDisplay.PolarAxes.PolarTicksVisibility = 1
poissonpvdDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
poissonpvdDisplay.PolarAxes.TickLocation = 'Both'
poissonpvdDisplay.PolarAxes.AxisTickVisibility = 1
poissonpvdDisplay.PolarAxes.AxisMinorTickVisibility = 0
poissonpvdDisplay.PolarAxes.ArcTickVisibility = 1
poissonpvdDisplay.PolarAxes.ArcMinorTickVisibility = 0
poissonpvdDisplay.PolarAxes.DeltaAngleMajor = 10.0
poissonpvdDisplay.PolarAxes.DeltaAngleMinor = 5.0
poissonpvdDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
poissonpvdDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
poissonpvdDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
poissonpvdDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
poissonpvdDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
poissonpvdDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
poissonpvdDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
poissonpvdDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
poissonpvdDisplay.PolarAxes.ArcMajorTickSize = 0.0
poissonpvdDisplay.PolarAxes.ArcTickRatioSize = 0.3
poissonpvdDisplay.PolarAxes.ArcMajorTickThickness = 1.0
poissonpvdDisplay.PolarAxes.ArcTickRatioThickness = 0.5
poissonpvdDisplay.PolarAxes.Use2DMode = 0
poissonpvdDisplay.PolarAxes.UseLogAxis = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
poissonpvdDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
poissonpvdDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera()

#changing interaction mode based on data extents
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.5, 0.5, 10000.0]
renderView1.CameraFocalPoint = [0.5, 0.5, 0.0]

# show color bar/color legend
poissonpvdDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Hide orientation axes
renderView1.OrientationAxesVisibility = 0

# get color legend/bar for f_253LUT in view renderView1
f_253LUTColorBar = GetScalarBar(f_253LUT, renderView1)

# change scalar bar placement
f_253LUTColorBar.WindowLocation = 'AnyLocation'
f_253LUTColorBar.Position = [0.8535980148883375, 0.2685560053981107]
f_253LUTColorBar.ScalarBarLength = 0.33

# change representation type
poissonpvdDisplay.SetRepresentationType('Surface With Edges')

# change representation type
poissonpvdDisplay.SetRepresentationType('Wireframe')

# change representation type
poissonpvdDisplay.SetRepresentationType('Points')

# change representation type
poissonpvdDisplay.SetRepresentationType('Surface')

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.5615142915342795, 0.5220820533712804, 10000.0]
renderView1.CameraFocalPoint = [0.5615142915342795, 0.5220820533712804, 0.0]
renderView1.CameraParallelScale = 0.584385769575659

# save screenshot
SaveScreenshot(str(png_output), renderView1, ImageResolution=[1024, 1024],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='',
    StereoMode='No change',
    TransparentBackground=0,
    ImageQuality=100)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.5615142915342795, 0.5220820533712804, 10000.0]
renderView1.CameraFocalPoint = [0.5615142915342795, 0.5220820533712804, 0.0]
renderView1.CameraParallelScale = 0.584385769575659

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
