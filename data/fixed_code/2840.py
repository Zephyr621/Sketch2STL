import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.6346 * 0.75)
    .threePointArc((0.0689 * 0.75, 0.0), (0.6874 * 0.75, 0.6346 * 0.75))
    .lineTo(0.6874 * 0.75, 0.5937 * 0.75)
    .threePointArc((0.7478 * 0.75, 0.6307 * 0.75), (0.75 * 0.75, 0.5937 * 0.75))
    .lineTo(0.75 * 0.75, 0.6346 * 0.75)
    .threePointArc((0.7478 * 0.75, 0.5899 * 0.75), (0.6874 * 0.75, 0.6346 * 0.75))
    .lineTo(0.6874 * 0.75, 0.6346 * 0.75)
    .threePointArc((0.7478 * 0.75, 0.6288 * 0.75), (0.6874 * 0.75, 0.5937 * 0.75))
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2840.stl