import cadquery as cq
from cadquery.vis import show
# --- Part 1: Hexagonal Prism ---
sketch_scale = 0.75
height = 0.0078
# Scaled coordinates for the hexagon
points = [
    (0.0 * sketch_scale, 0.3248 * sketch_scale),
    (0.1875 * sketch_scale, 0.0 * sketch_scale),
    (0.5625 * sketch_scale, 0.0 * sketch_scale),
    (0.75 * sketch_scale, 0.3248 * sketch_scale),
    (0.5625 * sketch_scale, 0.6495 * sketch_scale),
    (0.1875 * sketch_scale, 0.6495 * sketch_scale)
]
# Create the hexagonal base
part_1 = (
    cq.Workplane("XY")
    .polyline(points)
    .close()
    .extrude(height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0078, 0))
# --- Assembly ---
assembly = part
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2771.stl