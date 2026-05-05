import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .threePointArc((0.0278 * 0.75, 0.0156 * 0.75), (0.0388 * 0.75, 0.0))
    .lineTo(0.7159 * 0.75, 0.0)
    .threePointArc((0.7444 * 0.75, 0.0156 * 0.75), (0.75 * 0.75, 0.0))
    .lineTo(0.75 * 0.75, 0.1875 * 0.75)
    .threePointArc((0.7444 * 0.75, 0.3125 * 0.75), (0.7159 * 0.75, 0.375 * 0.75))
    .lineTo(0.0388 * 0.75, 0.375 * 0.75)
    .threePointArc((0.0278 * 0.75, 0.3125 * 0.75), (0.0, 0.1875 * 0.75))
    .lineTo(0.0, 0.0)
    .close()
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_879.stl