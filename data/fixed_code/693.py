import cadquery as cq
from cadquery.vis import show
# --- Part 1: L-shaped CAD Model ---
sketch_scale = 0.75
extrude_depth = 0.1339 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.6062 * sketch_scale)
    .lineTo(0.2308 * sketch_scale, 0.6062 * sketch_scale)
    .lineTo(0.2308 * sketch_scale, 0.6387 * sketch_scale)
    .lineTo(0.375 * sketch_scale, 0.6387 * sketch_scale)
    .lineTo(0.375 * sketch_scale, 0.6062 * sketch_scale)
    .lineTo(0.75 * sketch_scale, 0.6062 * sketch_scale)
    .lineTo(0.75 * sketch_scale, 0.6062 * sketch_scale)
    .lineTo(0.375 * sketch_scale, 0.6062 * sketch_scale)
    .lineTo(0.0, 0.6062 * sketch_scale)
    .close()
    .extrude(extrude_depth)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_693.stl