import cadquery as cq
from math import tan, radians, sqrt
# --- Parameters from JSON ---
sketch_scale = 0.75
outer_radius = 0.3248 * sketch_scale
inner_radius = 0.1695 * sketch_scale
height = 0.0469
# --- Create Hexagon ---
hex_points = [
    (0.0, outer_radius),
    (outer_radius, 0.0),
    (outer_radius, inner_radius),
    (0.2945, outer_radius),
    (0.6495, outer_radius),
    (0.6495, inner_radius)
]
hex_face = cq.Workplane("XY")
for point in hex_points:
    hex_face = hex_face.lineTo(point[0], point[1])
    hex_face = hex_face.close()
# --- Extrude ---
result = hex_face.extrude(height)
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export
# 导出为STL文件
cq.exporters.export(result, "output_3555.stl