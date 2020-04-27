import os.path

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

xdmf_input = os.path.join(os.path.dirname(__file__), "..", "computation", "poisson.xdmf" )
png_output = os.path.join(os.path.dirname(__file__), "poisson_field.png" )

# create a new 'XDMF Reader'
poissonxdmf = XDMFReader(FileNames=[xdmf_input])
poissonxdmf.PointArrayStatus = ['f_253']

poissonxdmf.CellArrayStatus = []
poissonxdmf.SetStatus = []
poissonxdmf.GridStatus = []
poissonxdmf.Stride = [1, 1, 1]

# Properties modified on poissonxdmf
poissonxdmf.GridStatus = ['mesh']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1612, 741]

# get color transfer function/color map for 'f_253'
f_253LUT = GetColorTransferFunction('f_253')
f_253LUT.InterpretValuesAsCategories = 0
f_253LUT.ShowCategoricalColorsinDataRangeOnly = 0
f_253LUT.RescaleOnVisibilityChange = 0
f_253LUT.EnableOpacityMapping = 0
f_253LUT.RGBPoints = [1.0, 0.231373, 0.298039, 0.752941, 2.5, 0.865003, 0.865003, 0.865003, 4.0, 0.705882, 0.0156863, 0.14902]
f_253LUT.UseLogScale = 0
f_253LUT.ColorSpace = 'Diverging'
f_253LUT.UseBelowRangeColor = 0
f_253LUT.BelowRangeColor = [0.0, 0.0, 0.0]
f_253LUT.UseAboveRangeColor = 0
f_253LUT.AboveRangeColor = [1.0, 1.0, 1.0]
f_253LUT.NanColor = [1.0, 1.0, 0.0]
f_253LUT.Discretize = 1
f_253LUT.NumberOfTableValues = 256
f_253LUT.ScalarRangeInitialized = 1.0
f_253LUT.HSVWrap = 0
f_253LUT.VectorComponent = 0
f_253LUT.VectorMode = 'Magnitude'
f_253LUT.AllowDuplicateScalars = 1
f_253LUT.Annotations = []
f_253LUT.ActiveAnnotatedValues = []
f_253LUT.IndexedColors = []

# get opacity transfer function/opacity map for 'f_253'
f_253PWF = GetOpacityTransferFunction('f_253')
f_253PWF.Points = [1.0, 0.0, 0.5, 0.0, 4.0, 1.0, 0.5, 0.0]
f_253PWF.AllowDuplicateScalars = 1
f_253PWF.ScalarRangeInitialized = 1

# show data in view
poissonxdmfDisplay = Show(poissonxdmf, renderView1)
# trace defaults for the display properties.
poissonxdmfDisplay.Representation = 'Surface'
poissonxdmfDisplay.AmbientColor = [1.0, 1.0, 1.0]
poissonxdmfDisplay.ColorArrayName = ['POINTS', 'f_253']
poissonxdmfDisplay.DiffuseColor = [1.0, 1.0, 1.0]
poissonxdmfDisplay.LookupTable = f_253LUT
poissonxdmfDisplay.MapScalars = 1
poissonxdmfDisplay.InterpolateScalarsBeforeMapping = 1
poissonxdmfDisplay.Opacity = 1.0
poissonxdmfDisplay.PointSize = 2.0
poissonxdmfDisplay.LineWidth = 1.0
poissonxdmfDisplay.Interpolation = 'Gouraud'
poissonxdmfDisplay.Specular = 0.0
poissonxdmfDisplay.SpecularColor = [1.0, 1.0, 1.0]
poissonxdmfDisplay.SpecularPower = 100.0
poissonxdmfDisplay.Ambient = 0.0
poissonxdmfDisplay.Diffuse = 1.0
poissonxdmfDisplay.EdgeColor = [0.0, 0.0, 0.5]
poissonxdmfDisplay.BackfaceRepresentation = 'Follow Frontface'
poissonxdmfDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
poissonxdmfDisplay.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
poissonxdmfDisplay.BackfaceOpacity = 1.0
poissonxdmfDisplay.Position = [0.0, 0.0, 0.0]
poissonxdmfDisplay.Scale = [1.0, 1.0, 1.0]
poissonxdmfDisplay.Orientation = [0.0, 0.0, 0.0]
poissonxdmfDisplay.Origin = [0.0, 0.0, 0.0]
poissonxdmfDisplay.Pickable = 1
poissonxdmfDisplay.Texture = None
poissonxdmfDisplay.Triangulate = 0
poissonxdmfDisplay.NonlinearSubdivisionLevel = 1
poissonxdmfDisplay.UseDataPartitions = 0
poissonxdmfDisplay.OSPRayUseScaleArray = 0
poissonxdmfDisplay.OSPRayScaleArray = 'f_253'
poissonxdmfDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
poissonxdmfDisplay.Orient = 0
poissonxdmfDisplay.OrientationMode = 'Direction'
poissonxdmfDisplay.SelectOrientationVectors = 'None'
poissonxdmfDisplay.Scaling = 0
poissonxdmfDisplay.ScaleMode = 'No Data Scaling Off'
poissonxdmfDisplay.ScaleFactor = 0.1
poissonxdmfDisplay.SelectScaleArray = 'f_253'
poissonxdmfDisplay.GlyphType = 'Arrow'
poissonxdmfDisplay.UseGlyphTable = 0
poissonxdmfDisplay.GlyphTableIndexArray = 'f_253'
poissonxdmfDisplay.UseCompositeGlyphTable = 0
poissonxdmfDisplay.DataAxesGrid = 'GridAxesRepresentation'
poissonxdmfDisplay.SelectionCellLabelBold = 0
poissonxdmfDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
poissonxdmfDisplay.SelectionCellLabelFontFamily = 'Arial'
poissonxdmfDisplay.SelectionCellLabelFontSize = 18
poissonxdmfDisplay.SelectionCellLabelItalic = 0
poissonxdmfDisplay.SelectionCellLabelJustification = 'Left'
poissonxdmfDisplay.SelectionCellLabelOpacity = 1.0
poissonxdmfDisplay.SelectionCellLabelShadow = 0
poissonxdmfDisplay.SelectionPointLabelBold = 0
poissonxdmfDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
poissonxdmfDisplay.SelectionPointLabelFontFamily = 'Arial'
poissonxdmfDisplay.SelectionPointLabelFontSize = 18
poissonxdmfDisplay.SelectionPointLabelItalic = 0
poissonxdmfDisplay.SelectionPointLabelJustification = 'Left'
poissonxdmfDisplay.SelectionPointLabelOpacity = 1.0
poissonxdmfDisplay.SelectionPointLabelShadow = 0
poissonxdmfDisplay.PolarAxes = 'PolarAxesRepresentation'
poissonxdmfDisplay.ScalarOpacityFunction = f_253PWF
poissonxdmfDisplay.ScalarOpacityUnitDistance = 0.04419417382415923
poissonxdmfDisplay.SelectMapper = 'Projected tetra'
poissonxdmfDisplay.SamplingDimensions = [128, 128, 128]
poissonxdmfDisplay.UseFloatingPointFrameBuffer = 1
poissonxdmfDisplay.GaussianRadius = 0.05
poissonxdmfDisplay.ShaderPreset = 'Sphere'
poissonxdmfDisplay.Emissive = 0
poissonxdmfDisplay.ScaleByArray = 0
poissonxdmfDisplay.SetScaleArray = ['POINTS', 'f_253']
poissonxdmfDisplay.ScaleTransferFunction = 'PiecewiseFunction'
poissonxdmfDisplay.OpacityByArray = 0
poissonxdmfDisplay.OpacityArray = ['POINTS', 'f_253']
poissonxdmfDisplay.OpacityTransferFunction = 'PiecewiseFunction'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
poissonxdmfDisplay.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'Arrow' selected for 'GlyphType'
poissonxdmfDisplay.GlyphType.TipResolution = 6
poissonxdmfDisplay.GlyphType.TipRadius = 0.1
poissonxdmfDisplay.GlyphType.TipLength = 0.35
poissonxdmfDisplay.GlyphType.ShaftResolution = 6
poissonxdmfDisplay.GlyphType.ShaftRadius = 0.03
poissonxdmfDisplay.GlyphType.Invert = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
poissonxdmfDisplay.DataAxesGrid.XTitle = 'X Axis'
poissonxdmfDisplay.DataAxesGrid.YTitle = 'Y Axis'
poissonxdmfDisplay.DataAxesGrid.ZTitle = 'Z Axis'
poissonxdmfDisplay.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
poissonxdmfDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
poissonxdmfDisplay.DataAxesGrid.XTitleBold = 0
poissonxdmfDisplay.DataAxesGrid.XTitleItalic = 0
poissonxdmfDisplay.DataAxesGrid.XTitleFontSize = 12
poissonxdmfDisplay.DataAxesGrid.XTitleShadow = 0
poissonxdmfDisplay.DataAxesGrid.XTitleOpacity = 1.0
poissonxdmfDisplay.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
poissonxdmfDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
poissonxdmfDisplay.DataAxesGrid.YTitleBold = 0
poissonxdmfDisplay.DataAxesGrid.YTitleItalic = 0
poissonxdmfDisplay.DataAxesGrid.YTitleFontSize = 12
poissonxdmfDisplay.DataAxesGrid.YTitleShadow = 0
poissonxdmfDisplay.DataAxesGrid.YTitleOpacity = 1.0
poissonxdmfDisplay.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
poissonxdmfDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
poissonxdmfDisplay.DataAxesGrid.ZTitleBold = 0
poissonxdmfDisplay.DataAxesGrid.ZTitleItalic = 0
poissonxdmfDisplay.DataAxesGrid.ZTitleFontSize = 12
poissonxdmfDisplay.DataAxesGrid.ZTitleShadow = 0
poissonxdmfDisplay.DataAxesGrid.ZTitleOpacity = 1.0
poissonxdmfDisplay.DataAxesGrid.FacesToRender = 63
poissonxdmfDisplay.DataAxesGrid.CullBackface = 0
poissonxdmfDisplay.DataAxesGrid.CullFrontface = 1
poissonxdmfDisplay.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
poissonxdmfDisplay.DataAxesGrid.ShowGrid = 0
poissonxdmfDisplay.DataAxesGrid.ShowEdges = 1
poissonxdmfDisplay.DataAxesGrid.ShowTicks = 1
poissonxdmfDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
poissonxdmfDisplay.DataAxesGrid.AxesToLabel = 63
poissonxdmfDisplay.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
poissonxdmfDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
poissonxdmfDisplay.DataAxesGrid.XLabelBold = 0
poissonxdmfDisplay.DataAxesGrid.XLabelItalic = 0
poissonxdmfDisplay.DataAxesGrid.XLabelFontSize = 12
poissonxdmfDisplay.DataAxesGrid.XLabelShadow = 0
poissonxdmfDisplay.DataAxesGrid.XLabelOpacity = 1.0
poissonxdmfDisplay.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
poissonxdmfDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
poissonxdmfDisplay.DataAxesGrid.YLabelBold = 0
poissonxdmfDisplay.DataAxesGrid.YLabelItalic = 0
poissonxdmfDisplay.DataAxesGrid.YLabelFontSize = 12
poissonxdmfDisplay.DataAxesGrid.YLabelShadow = 0
poissonxdmfDisplay.DataAxesGrid.YLabelOpacity = 1.0
poissonxdmfDisplay.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
poissonxdmfDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
poissonxdmfDisplay.DataAxesGrid.ZLabelBold = 0
poissonxdmfDisplay.DataAxesGrid.ZLabelItalic = 0
poissonxdmfDisplay.DataAxesGrid.ZLabelFontSize = 12
poissonxdmfDisplay.DataAxesGrid.ZLabelShadow = 0
poissonxdmfDisplay.DataAxesGrid.ZLabelOpacity = 1.0
poissonxdmfDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
poissonxdmfDisplay.DataAxesGrid.XAxisPrecision = 2
poissonxdmfDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
poissonxdmfDisplay.DataAxesGrid.XAxisLabels = []
poissonxdmfDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
poissonxdmfDisplay.DataAxesGrid.YAxisPrecision = 2
poissonxdmfDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
poissonxdmfDisplay.DataAxesGrid.YAxisLabels = []
poissonxdmfDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
poissonxdmfDisplay.DataAxesGrid.ZAxisPrecision = 2
poissonxdmfDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
poissonxdmfDisplay.DataAxesGrid.ZAxisLabels = []

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
poissonxdmfDisplay.PolarAxes.Visibility = 0
poissonxdmfDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
poissonxdmfDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
poissonxdmfDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
poissonxdmfDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
poissonxdmfDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
poissonxdmfDisplay.PolarAxes.EnableCustomRange = 0
poissonxdmfDisplay.PolarAxes.CustomRange = [0.0, 1.0]
poissonxdmfDisplay.PolarAxes.PolarAxisVisibility = 1
poissonxdmfDisplay.PolarAxes.RadialAxesVisibility = 1
poissonxdmfDisplay.PolarAxes.DrawRadialGridlines = 1
poissonxdmfDisplay.PolarAxes.PolarArcsVisibility = 1
poissonxdmfDisplay.PolarAxes.DrawPolarArcsGridlines = 1
poissonxdmfDisplay.PolarAxes.NumberOfRadialAxes = 0
poissonxdmfDisplay.PolarAxes.AutoSubdividePolarAxis = 1
poissonxdmfDisplay.PolarAxes.NumberOfPolarAxis = 0
poissonxdmfDisplay.PolarAxes.MinimumRadius = 0.0
poissonxdmfDisplay.PolarAxes.MinimumAngle = 0.0
poissonxdmfDisplay.PolarAxes.MaximumAngle = 90.0
poissonxdmfDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
poissonxdmfDisplay.PolarAxes.Ratio = 1.0
poissonxdmfDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
poissonxdmfDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
poissonxdmfDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
poissonxdmfDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
poissonxdmfDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
poissonxdmfDisplay.PolarAxes.PolarAxisTitleVisibility = 1
poissonxdmfDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
poissonxdmfDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
poissonxdmfDisplay.PolarAxes.PolarLabelVisibility = 1
poissonxdmfDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
poissonxdmfDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
poissonxdmfDisplay.PolarAxes.RadialLabelVisibility = 1
poissonxdmfDisplay.PolarAxes.RadialLabelFormat = '%-#3.1f'
poissonxdmfDisplay.PolarAxes.RadialLabelLocation = 'Bottom'
poissonxdmfDisplay.PolarAxes.RadialUnitsVisibility = 1
poissonxdmfDisplay.PolarAxes.ScreenSize = 10.0
poissonxdmfDisplay.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
poissonxdmfDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
poissonxdmfDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
poissonxdmfDisplay.PolarAxes.PolarAxisTitleBold = 0
poissonxdmfDisplay.PolarAxes.PolarAxisTitleItalic = 0
poissonxdmfDisplay.PolarAxes.PolarAxisTitleShadow = 0
poissonxdmfDisplay.PolarAxes.PolarAxisTitleFontSize = 12
poissonxdmfDisplay.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
poissonxdmfDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
poissonxdmfDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
poissonxdmfDisplay.PolarAxes.PolarAxisLabelBold = 0
poissonxdmfDisplay.PolarAxes.PolarAxisLabelItalic = 0
poissonxdmfDisplay.PolarAxes.PolarAxisLabelShadow = 0
poissonxdmfDisplay.PolarAxes.PolarAxisLabelFontSize = 12
poissonxdmfDisplay.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
poissonxdmfDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
poissonxdmfDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
poissonxdmfDisplay.PolarAxes.LastRadialAxisTextBold = 0
poissonxdmfDisplay.PolarAxes.LastRadialAxisTextItalic = 0
poissonxdmfDisplay.PolarAxes.LastRadialAxisTextShadow = 0
poissonxdmfDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
poissonxdmfDisplay.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
poissonxdmfDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
poissonxdmfDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
poissonxdmfDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
poissonxdmfDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
poissonxdmfDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
poissonxdmfDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
poissonxdmfDisplay.PolarAxes.EnableDistanceLOD = 1
poissonxdmfDisplay.PolarAxes.DistanceLODThreshold = 0.7
poissonxdmfDisplay.PolarAxes.EnableViewAngleLOD = 1
poissonxdmfDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
poissonxdmfDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
poissonxdmfDisplay.PolarAxes.PolarTicksVisibility = 1
poissonxdmfDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
poissonxdmfDisplay.PolarAxes.TickLocation = 'Both'
poissonxdmfDisplay.PolarAxes.AxisTickVisibility = 1
poissonxdmfDisplay.PolarAxes.AxisMinorTickVisibility = 0
poissonxdmfDisplay.PolarAxes.ArcTickVisibility = 1
poissonxdmfDisplay.PolarAxes.ArcMinorTickVisibility = 0
poissonxdmfDisplay.PolarAxes.DeltaAngleMajor = 10.0
poissonxdmfDisplay.PolarAxes.DeltaAngleMinor = 5.0
poissonxdmfDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
poissonxdmfDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
poissonxdmfDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
poissonxdmfDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
poissonxdmfDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
poissonxdmfDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
poissonxdmfDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
poissonxdmfDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
poissonxdmfDisplay.PolarAxes.ArcMajorTickSize = 0.0
poissonxdmfDisplay.PolarAxes.ArcTickRatioSize = 0.3
poissonxdmfDisplay.PolarAxes.ArcMajorTickThickness = 1.0
poissonxdmfDisplay.PolarAxes.ArcTickRatioThickness = 0.5
poissonxdmfDisplay.PolarAxes.Use2DMode = 0
poissonxdmfDisplay.PolarAxes.UseLogAxis = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
poissonxdmfDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
poissonxdmfDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera()

#changing interaction mode based on data extents
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.5, 0.5, 10000.0]
renderView1.CameraFocalPoint = [0.5, 0.5, 0.0]

# show color bar/color legend
poissonxdmfDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.Visibility = 1

# get color legend/bar for f_253LUT in view renderView1
f_253LUTColorBar = GetScalarBar(f_253LUT, renderView1)
f_253LUTColorBar.AutoOrient = 1
f_253LUTColorBar.Orientation = 'Vertical'
f_253LUTColorBar.WindowLocation = 'LowerRightCorner'
f_253LUTColorBar.Position = [0.89, 0.02]
f_253LUTColorBar.Title = 'f_253'
f_253LUTColorBar.ComponentTitle = ''
f_253LUTColorBar.TitleJustification = 'Centered'
f_253LUTColorBar.TitleColor = [0.0, 0.0, 0.0]
f_253LUTColorBar.TitleOpacity = 1.0
f_253LUTColorBar.TitleFontFamily = 'Arial'
f_253LUTColorBar.TitleBold = 0
f_253LUTColorBar.TitleItalic = 0
f_253LUTColorBar.TitleShadow = 0
f_253LUTColorBar.TitleFontSize = 16
f_253LUTColorBar.LabelColor = [0.0, 0.0, 0.0]
f_253LUTColorBar.LabelOpacity = 1.0
f_253LUTColorBar.LabelFontFamily = 'Arial'
f_253LUTColorBar.LabelBold = 0
f_253LUTColorBar.LabelItalic = 0
f_253LUTColorBar.LabelShadow = 0
f_253LUTColorBar.LabelFontSize = 16
f_253LUTColorBar.AutomaticLabelFormat = 1
f_253LUTColorBar.LabelFormat = '%-#6.3g'
f_253LUTColorBar.DrawTickMarks = 1
f_253LUTColorBar.DrawTickLabels = 1
f_253LUTColorBar.UseCustomLabels = 0
f_253LUTColorBar.CustomLabels = []
f_253LUTColorBar.AddRangeLabels = 1
f_253LUTColorBar.RangeLabelFormat = '%-#6.1e'
f_253LUTColorBar.DrawAnnotations = 1
f_253LUTColorBar.AddRangeAnnotations = 0
f_253LUTColorBar.AutomaticAnnotations = 0
f_253LUTColorBar.DrawNanAnnotation = 0
f_253LUTColorBar.NanAnnotation = 'NaN'
f_253LUTColorBar.TextPosition = 'Ticks right/top, annotations left/bottom'
f_253LUTColorBar.ScalarBarThickness = 16
f_253LUTColorBar.ScalarBarLength = 0.33

# change scalar bar placement
f_253LUTColorBar.WindowLocation = 'AnyLocation'
f_253LUTColorBar.Position = [0.7338709677419354, 0.08906882591093117]
f_253LUTColorBar.ScalarBarLength = 0.33000000000000007

# Hide orientation axes
renderView1.OrientationAxesVisibility = 0

# change scalar bar placement
f_253LUTColorBar.Position = [0.8327235714489081, 0.09716599190283397]
f_253LUTColorBar.ScalarBarLength = 0.3300000000000001

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.XTitleFontSize = 16
renderView1.AxesGrid.YTitleFontSize = 16
renderView1.AxesGrid.ZTitleFontSize = 16
renderView1.AxesGrid.XLabelFontSize = 16
renderView1.AxesGrid.YLabelFontSize = 16
renderView1.AxesGrid.ZLabelFontSize = 16

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.5, 0.5, 10000.0]
renderView1.CameraFocalPoint = [0.5, 0.5, 0.0]
renderView1.CameraParallelScale = 0.584385769575659

# save screenshot
SaveScreenshot(png_output, renderView1, ImageResolution=[1133, 741],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='',
    StereoMode='No change',
    TransparentBackground=0,
    ImageQuality=100)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.5, 0.5, 10000.0]
renderView1.CameraFocalPoint = [0.5, 0.5, 0.0]
renderView1.CameraParallelScale = 0.584385769575659

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
