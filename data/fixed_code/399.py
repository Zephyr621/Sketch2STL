import cadquery as cq
from cadquery.vis import show
# --- Part 1: Curved Shape with Holes ---
sketch_scale = 0.75
extrude_depth = 0.0312 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .threePointArc((0.375 * sketch_scale, 0.0313 * sketch_scale), (0.7188 * sketch_scale, 0.0))
    .lineTo(0.75 * sketch_scale, 0.0)
    .threePointArc((0.75 * sketch_scale, 0.1253 * sketch_scale), (0.7188 * sketch_scale, 0.25 * sketch_scale))
    .lineTo(0.0, 0.25 * sketch_scale)
    .threePointArc((0.0105 * sketch_scale, 0.1253 * sketch_scale), (0.0, 0.0))
    .close()
    .add(cq.Workplane("XY").circle(0.0061 * sketch_scale).val().move(cq.Location(cq.Vector(0.4687 * sketch_scale, 0.2038 * sketch_scale, 0))))
    .add(cq.Workplane("XY").
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_399.stl