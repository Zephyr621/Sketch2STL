import cadquery as cq
from math import tan, radians
# --- Part 1: Hexagonal Prism ---
sketch_scale = 0.75
height = 0.0019 * 2  # Total extrusion depth (towards + opposite normal)
# Scaled coordinates for the hexagon
points = [
    (0.0, 0.3248),
    (0.1875, 0.0),
    (0.5625, 0.0),
    (0.75, 0.3248),
    (0.5625, 0.6495),
    (0.1875, 0.6495)
]
scaled_points = [(x * sketch_scale, y * sketch_scale) for x, y in points]
part_1 = (
    cq.Workplane("XY")
    .polyline(scaled_points)
    .close()
    .extrude(height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0139 * sketch_scale, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.cq.exporters.export(assembly
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_393.stl