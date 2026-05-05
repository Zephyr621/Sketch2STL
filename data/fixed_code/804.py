import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.0067
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0 * sketch_scale, 0.0184 * sketch_scale)
    .threePointArc((0.0006 * sketch_scale, 0.0006 * sketch_scale), (0.0184 * sketch_scale, 0.0 * sketch_scale))
    .lineTo(0.7498 * sketch_scale, 0.0 * sketch_scale)
    .threePointArc((0.7416 * sketch_scale, 0.0006 * sketch_scale), (0.75 * sketch_scale, 0.0184 * sketch_scale))
    .lineTo(0.75 * sketch_scale, 0.0268 * sketch_scale)
    .threePointArc((0.7416 * sketch_scale, 0.0254 * sketch_scale), (0.7498 * sketch_scale, 0.0268 * sketch_scale))
    .lineTo(0.0184 * sketch_scale, 0.0268 * sketch_scale)
    .threePointArc((0.0006 * sketch_scale, 0.0254 * sketch_scale), (0.0 * sketch_scale, 0.0268 * sketch_scale))
    .lineTo(0.0 * sketch_
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_804.stl