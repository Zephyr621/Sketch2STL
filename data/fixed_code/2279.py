import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder ---
sketch_scale = 0.75
# Scaled coordinates
p1 = (0.0 * sketch_scale, 0.0156 * sketch_scale)
p2 = (0.0038 * sketch_scale, 0.0 * sketch_scale)
p3 = (0.7188 * sketch_scale, 0.0156 * sketch_scale)
p4 = (0.7188 * sketch_scale, 0.0312 * sketch_scale)
p5 = (0.75 * sketch_scale, 0.0313 * sketch_scale)
p6 = (0.75 * sketch_scale, 0.0562 * sketch_scale)
p7 = (0.7188 * sketch_scale, 0.0469 * sketch_scale)
p8 = (0.7188 * sketch_scale, 0.0294 * sketch_scale)
p9 = (0.7188 * sketch_scale, 0.0156 * sketch_scale)
p10 = (0.0038 * sketch_scale, 0.0156 * sketch_scale)
p11 = (0.0 * sketch_scale, 0.0313 * sketch_scale)
part_1 = (
    cq.Workplane("XY")
    .moveTo(p1[0], p1[1])
    .threePointArc((0.0176 * sketch_scale, 0
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2279.stl