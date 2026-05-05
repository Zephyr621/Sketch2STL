import cadquery as cq
from cadquery.vis import show
# --- Part 1: Rectangular Block with Rounded Edges ---
sketch_scale = 0.75
extrude_depth = 0.0937 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0469 * sketch_scale)
    .lineTo(0.0469 * sketch_scale, 0.0)
    .threePointArc((0.375 * sketch_scale, 0.0208 * sketch_scale), (0.7499 * sketch_scale, 0.0469 * sketch_scale))
    .lineTo(0.7499 * sketch_scale, 0.0779 * sketch_scale)
    .threePointArc((0.375 * sketch_scale, 0.1822 * sketch_scale), (0.2829 * sketch_scale, 0.0779 * sketch_scale))
    .lineTo(0.2829 * sketch_scale, 0.375 * sketch_scale)
    .lineTo(0.0469 * sketch_scale, 0.375 * sketch_scale)
    .threePointArc((0.0, 0.1822 * sketch_scale), (0.0, 0.0469 * sketch_scale))
    .close()
    .extrude(extrude_depth)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_312.stl