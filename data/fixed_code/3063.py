import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .threePointArc((0.7188, 0.3879), (0.7321, 0.6185))
    .lineTo(0.6484, 0.6185)
    .lineTo(0.6484, 0.4432)
    .lineTo(0.4773, 0.4432)
    .threePointArc((0.2435, 0.3755), (0.1266, 0.3928))
    .lineTo(0.0011, 0.3928)
    .lineTo(0.0, 0.4432)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.1644)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.1644))
# --- Assembly ---
assembly = part_1
cq.
cq
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3063.stl