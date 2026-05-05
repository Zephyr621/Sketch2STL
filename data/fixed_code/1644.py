import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.0234 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.7188 * sketch_scale, 0.0)
    .threePointArc((0.75 * sketch_scale, 0.1406 * sketch_scale), (0.7188 * sketch_scale, 0.2812 * sketch_scale))
    .lineTo(0.0, 0.2812 * sketch_scale)
    .lineTo(0.0, 0.0)
    .close()
    .moveTo(0.0469 * sketch_scale, 0.0469 * sketch_scale)
    .threePointArc((0.0, 0.1406 * sketch_scale), (0.0469 * sketch_scale, 0.0469 * sketch_scale))
    .lineTo(0.0469 * sketch_scale, 0.1875 * sketch_scale)
    .threePointArc((0.0469 * sketch_scale, 0.2813 * sketch_scale), (0.0469 * sketch_scale, 0.
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1644.stl