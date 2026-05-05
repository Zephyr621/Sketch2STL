import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.15 * 0.75)
    .lineTo(0.0195 * 0.75, 0.15 * 0.75)
    .threePointArc((0.375 * 0.75, 0.0), (0.5754 * 0.75, 0.15 * 0.75))
    .lineTo(0.75 * 0.75, 0.15 * 0.75)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.6346 * 0.75, 0.0)
    .lineTo(0.6346 * 0.75, 0.15 * 0.75)
    .lineTo(0.75 * 0.75, 0.3948 * 0.75)
    .lineTo(0.7031 * 0.75, 0.3948 * 0.75)
    .threePointArc((0.375 * 0.75, 0.3948 * 0.75), (0.1058 * 0.75, 0.3948 * 0.75))
    .lineTo(0.0, 0.15 * 0.75)
    .close()
    .extrude(0.1167)
)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3471.stl