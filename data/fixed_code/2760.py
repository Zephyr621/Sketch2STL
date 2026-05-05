import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .threePointArc((0.75 * 0.75, 0.067 * 0.75), (0.75 * 0.75, 0.1239 * 0.75))
    .lineTo(0.6977 * 0.75, 0.1239 * 0.75)
    .threePointArc((0.6822 * 0.75, 0.0893 * 0.75), (0.6977 * 0.75, 0.0))
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.0682 * 0.75)
    .threePointArc((0.6822 * 0.75, 0.0603 * 0.75), (0.6977 * 0.75, 0.1073 * 0.75))
    .lineTo(0.6977 * 0.75, 0.1314 * 0.75)
    .threePointArc((0.6822 * 0.75, 0.1324 * 0.75), (0.6977 * 0.75, 0.13
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2760.stl