import cadquery as cq
from math import radians
# --- Part 1: Rectangular Block with U-shaped Cutout ---
part_1_width = 0.3724 * 0.75
part_1_height = 0.3724
part_1_depth = 0.1293
sketch_scale = 0.75
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(part_1_width, 0)
    .lineTo(part_1_width, part_1_height)
    .lineTo(0.0384 * sketch_scale, part_1_height)
    .threePointArc((0.0938 * sketch_scale, 0.0938 * sketch_scale), (0.0384 * sketch_scale, part_1_height))
    .lineTo(0, 0.0384 * sketch_scale)
    .close()
    .extrude(part_1_depth)
)
# --- Part 2: Cylinder Cutout ---
part_2_radius = 0.0682 * 0.1364
part_2_depth = 0.1293
sketch_scale_2 = 0.1364
part_2 = (
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1313.stl