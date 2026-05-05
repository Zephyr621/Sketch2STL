import cadquery as cq
from cadquery.vis import show
# --- Part 1: L-shaped CAD Model ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.0933)
    .threePointArc((0.375, 0.0417), (0.375, 0.0933))
    .lineTo(0.0, 0.0933)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0183)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0183, 0))
# --- Assembly ---
assembly = part_1
cq.
# Export to STL
cq.
# Export to STL
cq
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1039.stl