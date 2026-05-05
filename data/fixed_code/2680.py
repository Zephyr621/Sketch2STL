import cadquery as cq
# --- Part 1: Rectangular Block with Notch ---
length = 0.75 * 0.75  # Scaled length
width = 0.3193 * 0.75  # Scaled width
height = 0.0509
notch_x1 = 0.0534 * 0.75  # Scaled x-coordinate
notch_y1 = 0.1554 * 0.75  # Scaled y-coordinate
notch_x2 = 0.6977 * 0.75  # Scaled x-coordinate
notch_y2 = 0.1639 * 0.75  # Scaled y-coordinate
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(length, 0)
    .lineTo(length, width)
    .lineTo(notch_x1, width)
    .lineTo(notch_x1, notch_y1)
    .lineTo(0, notch_y1)
    .close()
    .extrude(height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0509, 0))
# --- Assembly ---
assembly = part_1
#
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2680.stl