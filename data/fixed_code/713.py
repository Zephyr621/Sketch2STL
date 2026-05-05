import cadquery as cq
from cadquery.vis import show
# --- Part 1: S shaped Object ---
sketch_scale = 0.75
extrude_depth = 0.1071 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0964 * sketch_scale)
    .lineTo(0.0468 * sketch_scale, 0.0964 * sketch_scale)
    .threePointArc((0.375 * sketch_scale, 0.2893 * sketch_scale), (0.3214 * sketch_scale, 0.0))
    .lineTo(0.75 * sketch_scale, 0.0)
    .lineTo(0.75 * sketch_scale, 0.2143 * sketch_scale)
    .lineTo(0.5636 * sketch_scale, 0.2143 * sketch_scale)
    .lineTo(0.5636 * sketch_scale, 0.0964 * sketch_scale)
    .lineTo(0.0468 * sketch_scale, 0.0964 * sketch_scale)
    .close()
    .extrude(extrude_depth)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_713.stl