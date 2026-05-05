import cadquery as cq
from math import radians
# --- Part 1: Rectangular Plate ---
part_1_length = 0.45 * 0.75
part_1_width = 0.75 * 0.75
part_1_height = 0.0118
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Part 2: Curved Cutout ---
part_2_depth = 0.0326
sketch_scale = 0.6511
part_2 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.1748 * sketch_scale, 0.0)
    .threePointArc((0.2604 * sketch_scale, 0.0299 * sketch_scale), (0.2624 * sketch_scale, 0.0982 * sketch_scale))
    .lineTo(0.3949 * sketch_scale, 0.6511 * sketch_scale)
    .threePointArc((0.4706 * sketch_scale, 0.7125 * sketch_scale), (0.4496 * sketch_scale, 0.6511 * sketch_scale))
    .lineTo(
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2676.stl