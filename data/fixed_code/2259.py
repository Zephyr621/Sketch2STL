import cadquery as cq
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_height = 0.1442
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.1442, 0))
# --- Part 2: Cut Feature ---
sketch_scale_part2 = 0.375
part_2_depth = 0.1442
cut_feature = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.375 * sketch_scale_part2)
    .threePointArc((0.1875 * sketch_scale_part2, 0.0), (0.375 * sketch_scale_part2, 0.0))
    .lineTo(0.375 * sketch_scale_part2, 0.375 * sketch_scale_part2)
    .close()
)
cut_feature2 = (
    cq.Workplane("XY")
    .moveTo(0.375 * sketch_scale_part2
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_2259.stl