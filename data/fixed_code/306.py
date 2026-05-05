import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0729 * 0.75)
    .lineTo(0.0729 * 0.75, 0.0)
    .threePointArc((0.3772 * 0.75, 0.1406 * 0.75), (0.7149 * 0.75, 0.0))
    .lineTo(0.7149 * 0.75, 0.0729 * 0.75)
    .lineTo(0.75 * 0.75, 0.0729 * 0.75)
    .lineTo(0.75 * 0.75, 0.2397 * 0.75)
    .lineTo(0.7149 * 0.75, 0.2397 * 0.75)
    .lineTo(0.7149 * 0.75, 0.2812 * 0.75)
    .lineTo(0.0, 0.2812 * 0.75)
    .lineTo(0.0, 0.0729 * 0.75)
    .close()
    .extrude(0.0357)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_306.stl