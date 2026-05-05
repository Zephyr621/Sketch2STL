import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.0429
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0 * sketch_scale, 0.1389 * sketch_scale)
    .threePointArc((0.0949 * sketch_scale, 0.1792 * sketch_scale), (0.2721 * sketch_scale, 0.1389 * sketch_scale))
    .lineTo(0.2721 * sketch_scale, 0.3379 * sketch_scale)
    .lineTo(0.0 * sketch_scale, 0.3379 * sketch_scale)
    .close()
    .extrude(extrude_depth)
)
# --- Assembly ---
assembly = part_1
cq.
# Export to STL
cq.
cq.
cq.exporters.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1573.stl