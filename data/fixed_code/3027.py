import cadquery as cq
from math import *
# --- Parameters from JSON ---
length = 0.75
width = 0.2577
height = 0.0085
sketch_scale = 0.75
hole_radius = 0.0268
corner_radius = 0.05  # Assuming a corner radius for rounded corners
# Scale parameters
length *= sketch_scale
width *= sketch_scale
corner_radius *= sketch_scale
hole_radius *= sketch_scale
# --- Create the base plate ---
plate = (
    cq.Workplane("XY")
    .moveTo(0, corner_radius)
    .threePointArc((corner_radius, 0), (0.05 * sketch_scale, 0.05 * sketch_scale))
    .lineTo(length - corner_radius, 0)
    .threePointArc((length, corner_radius), (length - 0.05 * sketch_scale, 0.05 * sketch_scale))
    .lineTo(length, width - corner_radius)
    .threePointArc((length - corner_radius, width), (length - 0.05 * sketch_scale, width - 0.05 * sketch_scale))
    .lineTo(corner_radius, width)
    .threePointArc((0, width - corner_radius), (corner_radius, width - 0.05 * sketch_scale))
    .close()
    .extrude(height)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3027.stl