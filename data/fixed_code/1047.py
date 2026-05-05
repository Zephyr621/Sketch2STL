import cadquery as cq
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.2344 * 0.4351  # Sketch radius scaled
part_1_height = 0.75
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(-part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Part 2: Rectangular Cutout ---
sketch_scale_part2 = 0.2283
part_2_depth = 0.1461
part_2 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.2283 * sketch_scale_part2, 0.0)
    .lineTo(0.2283 * sketch_scale_part2, 0.0357 * sketch_scale_part2)
    .lineTo(0.0, 0.0357 * sketch_scale_part2)
    .close()
    .extrude(-part_2_depth)
)
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_1047.stl