import cadquery as cq
from cadquery.vis import show
# --- Part 1: L-shaped CAD Model ---
sketch_scale = 0.75
extrude_depth = 0.5357 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * sketch_scale, 0.0)
    .lineTo(0.75 * sketch_scale, 0.3214 * sketch_scale)
    .lineTo(0.2571 * sketch_scale, 0.3214 * sketch_scale)
    .lineTo(0.2571 * sketch_scale, 0.5357 * sketch_scale)
    .lineTo(0.0, 0.5357 * sketch_scale)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(extrude_depth)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.5357, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
#
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_662.stl