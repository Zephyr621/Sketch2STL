import cadquery as cq
# --- Parameters from JSON ---
length = 0.75
width = 0.2885
height = 0.0441
sketch_scale = 0.75
hole1_center = (0.0937, 0.1406)
hole1_radius = 0.0234
hole2_center = (0.6562, 0.1406)
hole2_radius = 0.0168
hole3_center = (0.5769, 0.1406)
hole3_radius = 0.0072
# Scale parameters
length *= sketch_scale
width *= sketch_scale
hole1_center = (hole1_center[0] * sketch_scale, hole1_center[1] * sketch_scale)
hole1_radius *= sketch_scale
hole2_center = (hole2_center[0] * sketch_scale, hole2_center[1] * sketch_scale)
hole2_radius *= sketch_scale
hole3_center = (hole3_center[0] * sketch_scale, hole3_center[1] * sketch_scale)
hole3_radius *= sketch_scale
# --- Create the base rectangular plate ---
plate = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Cut the holes ---
plate = (
    plate.faces(">Z
# Export
# 定义结果变量
result = plate
# 导出为STL文件
cq.exporters.export(result, "output_1939.stl