import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0017 * 0.75)
    .lineTo(0.0592 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.3701 * 0.75)
    .threePointArc((0.7061 * 0.75, 0.3635 * 0.75), (0.5524 * 0.75, 0.4641 * 0.75))
    .lineTo(0.0, 0.0017 * 0.75)
    .close()
    .extrude(0.0469)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0469, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.cq.exporters.export(assembly,
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_201.stl