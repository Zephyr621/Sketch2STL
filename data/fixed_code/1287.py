import cadquery as cq
from cadquery import exporters
# --- Part 1: Cylinder Base ---
part_1_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_height = 0.0862
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(-part_1_height)
# --- Part 2: Cutout ---
part_2_outer_radius = 0.3365 * 0.6709
part_2_inner_radius = 0.3173 * 0.6709
part_2_height = 0.0478
part_2 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.0811 * 0.6709, 0.0)
    .threePointArc((0.1664 * 0.6709, 0.0156 * 0.6709), (0.1739 * 0.6709, 0.0))
    .lineTo(0.6695 * 0.6709, 0.0)
    .threePointArc((0.5848 * 0.6709, 0.0156 * 0.6709), (0.6635 * 0.6709, 0.0521 * 0.6709))
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_1287.stl