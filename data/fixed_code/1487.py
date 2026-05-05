import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.5114 * 0.7122)
    .threePointArc((0.0148 * 0.7122, 0.3519 * 0.7122), (0.0441 * 0.7122, 0.5114 * 0.7122))
    .lineTo(0.3706 * 0.7122, 0.75 * 0.7122)
    .threePointArc((0.3743 * 0.7122, 0.3938 * 0.7122), (0.3092 * 0.7122, 0.0))
    .lineTo(0.3188 * 0.7122, 0.0)
    .threePointArc((0.1547 * 0.7122, 0.5115 * 0.7122), (0.1518 * 0.7122, 0.5117 * 0.7122))
    .lineTo(0.0361 * 0.7122, 0.7122 * 0.7122)
    .threePointArc((0.0769 * 0.7122, 0.3742 * 0.7122), (0.0, 0.5114 * 0.7122))
    .close()
    .extrude(0.0291)
)
# --- Assembly ---
assembly = part_1
cq.
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1487.stl