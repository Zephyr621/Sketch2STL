import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0977 * 0.75)
    .lineTo(0.1659 * 0.75, 0.0)
    .threePointArc((0.375 * 0.75, 0.1178 * 0.75), (0.5702 * 0.75, 0.0598 * 0.75))
    .lineTo(0.6596 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.0977 * 0.75)
    .lineTo(0.6328 * 0.75, 0.2128 * 0.75)
    .lineTo(0.5643 * 0.75, 0.2332 * 0.75)
    .lineTo(0.3741 * 0.75, 0.2332 * 0.75)
    .threePointArc((0.1201 * 0.75, 0.2328 * 0.75), (0.0824 * 0.75, 0.1807 * 0.75))
    .lineTo(0.0, 0.0977 * 0.75)
    .close()
    .extrude(0
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1737.stl