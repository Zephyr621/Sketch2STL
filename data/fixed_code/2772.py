import cadquery as cq
# --- Part 1: Cube with Cutout ---
length = 0.75 * 0.75  # Scaled length
width = 0.4 * 0.75  # Scaled width
height = 0.28
cutout_x = 0.0825 * 0.75  # Scaled cutout x
cutout_y = 0.2 * 0.75  # Scaled cutout y
cutout_width = (0.5 - 0.0825) * 0.75  # Scaled cutout width
cutout_height = (0.4 - 0.2) * 0.75  # Scaled cutout height
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
)
cutout = (
    cq.Workplane("XY")
    .moveTo(cutout_x - length/2, cutout_y - width/2)
    .rect(cutout_width, cutout_height)
    .extrude(height)
)
part_1 = part_1.cut(cutout)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.28, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2772.stl