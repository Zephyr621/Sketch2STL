import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0156 * 0.75)
    .threePointArc((0.0026 * 0.75, 0.0026 * 0.75), (0.0156 * 0.75, 0.0))
    .lineTo(0.7188 * 0.75, 0.0)
    .threePointArc((0.7419 * 0.75, 0.0026 * 0.75), (0.75 * 0.75, 0.0156 * 0.75))
    .lineTo(0.75 * 0.75, 0.2953 * 0.75)
    .threePointArc((0.7419 * 0.75, 0.3462 * 0.75), (0.7188 * 0.75, 0.3125 * 0.75))
    .lineTo(0.0156 * 0.75, 0.3125 * 0.75)
    .threePointArc((0.0026 * 0.75, 0.3462 * 0.75), (0.0, 0.2953 * 0.75))
    .lineTo(0.0, 0.
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2603.stl