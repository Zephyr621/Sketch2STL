import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0415 * 0.75)
    .threePointArc((0.0205 * 0.75, 0.0205 * 0.75), (0.0415 * 0.75, 0.0))
    .lineTo(0.6495 * 0.75, 0.0)
    .threePointArc((0.7295 * 0.75, 0.0205 * 0.75), (0.75 * 0.75, 0.0415 * 0.75))
    .lineTo(0.75 * 0.75, 0.6094 * 0.75)
    .threePointArc((0.7295 * 0.75, 0.6324 * 0.75), (0.6495 * 0.75, 0.6118 * 0.75))
    .lineTo(0.0415 * 0.75, 0.6118 * 0.75)
    .threePointArc((0.0205 * 0.75, 0.6324 * 0.75), (0.0, 0.6094 * 0.75))
    .lineTo(0.0, 0.0415 * 0.75)
    .close()
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2039.stl