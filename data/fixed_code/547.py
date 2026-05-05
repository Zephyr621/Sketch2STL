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
hole_center_x = 0.375
hole_center_y = 0.3248
hole_radius = 0.1094
sketch_scale = 0.75
# Scale parameters
outer_points_scaled = [(x * sketch_scale, y * sketch_scale) for x, y in outer_points]
hole_center_x *= sketch_scale
hole_center_y *= sketch_scale
hole_radius *= sketch_scale
# --- Create the Hexagonal base ---
hex_base = (
    cq.Workplane("XY")
    .polyline(outer_points_scaled)
    .close()
    .extrude(0.1262 * sketch_scale)
)
# --- Create the Hole ---
hole = (
    cq.Workplane("XY")
    .circle(hole_radius)
    .extrude(-0.1262 * sketch_scale)
)
# --- Subtract the Hole from the Base ---
result = hex
# Export
# 导出为STL文件
cq.exporters.export(result, "output_547.stl