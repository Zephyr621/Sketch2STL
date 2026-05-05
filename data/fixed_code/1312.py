import cadquery as cq
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_height = 0.0625
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0625, 0))
# --- Part 2: Holes ---
hole_radius = 0.0188 * 0.75
hole_depth = 0.0625
hole_centers = [
    (0.0188 * 0.75, 0.0188 * 0.75),
    (0.7188 * 0.75, 0.0188 * 0.75),
    (0.7188 * 0.75, 0.7188 * 0.75),
    (0.7188 * 0.75, 0.7188 * 0.75)
]
part_2 = cq.Workplane("XY")
for center in hole_centers:
    part_2 = part_2.moveTo(center[0], center[1]).circle(hole_radius)
part_2 = part_2.extrude(-hole_depth)
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_1312.stl