import cadquery as cq
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_height = 0.2812
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(-part_1_height)
# --- Part 2: Hole ---
hole_radius = 0.0703 * 0.1406
hole_depth = 0.0938
hole_locations = [
    (0.0703 * 0.1406 + 0.0938 * 0.1406, 0.0938 * 0.1406 + 0.6562 * 0.1406),
    (0.0703 * 0.1406 + 0.6562 * 0.1406, 0.0938 * 0.1406 + 0.6562 * 0.1406),
    (0.0703 * 0.1406 + 0.6281 * 0.1406, 0.0938 * 0.1406 + 0.6562 * 0.1406),
]
part_2 = cq.Workplane("XY")
for x, y in hole_locations:
    part_2 = part_2.moveTo(x, y).circle(hole_radius)
part_2 = part_2.extrude(-hole_depth)
# --- Part 3: Two Cylindrical Protrus
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_1354.stl