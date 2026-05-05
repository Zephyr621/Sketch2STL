import cadquery as cq
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_height = 0.0804
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0804, 0))
# --- Part 2: Cut Feature ---
cut_depth = 0.0352
sketch_scale = 0.0543
cut_locations = [
    (0.0183 * sketch_scale, 0.0183 * sketch_scale),
    (0.0183 * sketch_scale, 0.5262 * sketch_scale),
    (0.0183 * sketch_scale, 0.7125 * sketch_scale),
    (0.0288 * sketch_scale, 0.7125 * sketch_scale),
]
cut_part = cq.Workplane("XY")
for x, y in cut_locations:
    cut_part = cut_part.moveTo(x, y).circle(part_2_radius
# 定义结果变量
result = cut_part
# 导出为STL文件
cq.exporters.export(result, "output_897.stl