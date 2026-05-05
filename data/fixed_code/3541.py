import cadquery as cq
from math import tan, radians, sqrt
# --- Parameters from JSON ---
sketch_scale = 0.75
extrusion_depth = 0.1875
hole_center_x = 0.3248 * sketch_scale
hole_center_y = 0.375 * sketch_scale
hole_radius = 0.1562 * sketch_scale
# --- Create Hexagon ---
hexagon = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.1364 * sketch_scale)
    .lineTo(0.3248 * sketch_scale, 0.0)
    .lineTo(0.6495 * sketch_scale, 0.0)
    .lineTo(0.6495 * sketch_scale, 0.6196 * sketch_scale)
    .threePointArc((0.3248 * sketch_scale, 0.7011 * sketch_scale), (0.1038 * sketch_scale, 0.75 * sketch_scale))
    .lineTo(0.0, 0.1364 * sketch_scale)
    .close()
    .extrude(extrusion_depth)
)
# --- Create Hole ---
hole = (
    cq.Workplane("XY")
    .circle(hole_radius)
    .extrude(-extrusion_depth)
)
# --- Subtract Ho
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3541.stl