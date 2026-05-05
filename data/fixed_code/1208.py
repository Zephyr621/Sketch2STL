import cadquery as cq
from cadquery.vis import show
# --- Part 1: L-shaped CAD Model ---
sketch_scale = 0.75
extrude_depth = 0.3581 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.3116 * sketch_scale)
    .threePointArc((0.0055 * sketch_scale, 0.0055 * sketch_scale), (0.0, 0.3116 * sketch_scale))
    .lineTo(0.0, 0.4687 * sketch_scale)
    .lineTo(0.0, 0.5771 * sketch_scale)
    .lineTo(0.0577 * sketch_scale, 0.5771 * sketch_scale)
    .lineTo(0.0577 * sketch_scale, 0.4538 * sketch_scale)
    .lineTo(0.0, 0.4538 * sketch_scale)
    .lineTo(0.0, 0.3116 * sketch_scale)
    .close()
    .extrude(extrude_depth)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.2256))
# --- Assembly ---
assembly = part_1
# Export to ST
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1208.stl