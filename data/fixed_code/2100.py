import cadquery as cq
from cadquery.vis import show
# --- Part 1: Rectangular Block ---
sketch_scale = 0.75
extrude_depth = 0.0625
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0 * sketch_scale, 0.0312 * sketch_scale)
    .threePointArc((0.0156 * sketch_scale, 0.0156 * sketch_scale), (0.0312 * sketch_scale, 0.0 * sketch_scale))
    .lineTo(0.7188 * sketch_scale, 0.0 * sketch_scale)
    .threePointArc((0.7083 * sketch_scale, 0.0156 * sketch_scale), (0.75 * sketch_scale, 0.0312 * sketch_scale))
    .lineTo(0.75 * sketch_scale, 0.25 * sketch_scale)
    .threePointArc((0.7083 * sketch_scale, 0.2402 * sketch_scale), (0.7188 * sketch_scale, 0.25 * sketch_scale))
    .lineTo(0.0312 * sketch_scale, 0.25 * sketch_scale)
    .threePointArc((0.0156 * sketch_scale, 0.2402 * sketch_scale), (0.0 * sketch_scale, 0.0312
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2100.stl