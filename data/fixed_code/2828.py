import cadquery as cq
from cadquery.vis import show
# --- Part 1: Rectangular Box ---
length = 0.75 * 0.75  # Scaled length
width = 0.5719 * 0.75  # Scaled width
height = 0.2396
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(length, 0)
    .threePointArc((length + 0.0099 * 0.75, width), (0, 0))
    .close()
    .extrude(height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.2396, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2828.stl