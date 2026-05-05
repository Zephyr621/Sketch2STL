import cadquery as cq
from math import tan, radians
# --- Parameters from JSON ---
outer_points = [
    (0.0, 0.3248),
    (0.1875, 0.0),
    (0.5625, 0.0),
    (0.75, 0.3248),
    (0.5625, 0.6495),
    (0.1875, 0.6495)
]
inner_circle_center = (0.375, 0.3248)
inner_circle_radius = 0.1687
sketch_scale = 0.75
extrusion_depth = 0.1364
# Scale parameters
outer_points = [(x * sketch_scale, y * sketch_scale) for x, y in outer_points]
inner_circle_center = (inner_circle_center[0], inner_circle_center[1])
inner_circle_radius *= sketch_scale
# --- Create the Hexagon with Hole ---
hex_base = (
    cq.Workplane("XY")
    .polyline(outer_points)
    .close()
    .extrude(extrusion_depth)
)
# --- Create the Circular Hole ---
hole = (
    cq.Workplane("XY")
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2617.stl