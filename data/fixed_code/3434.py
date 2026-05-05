import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.1087)
    .threePointArc((0.6479, 0.2206), (0.5279, 0.2143))
    .lineTo(0.2542, 0.2143)
    .threePointArc((0.2062, 0.2206), (0.1532, 0.1087))
    .lineTo(0.0, 0.1087)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0804)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0804, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.exporters
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3434.stl