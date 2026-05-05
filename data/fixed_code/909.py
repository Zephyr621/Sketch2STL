import cadquery as cq
from cadquery.vis import show
# --- Part 1: Rectangular Object with Cutout ---
length = 0.75 * 0.75  # Scaled length
width = 0.4167 * 0.75  # Scaled width
height = 0.0121
cutout_x_start = 0.1767 * 0.75  # Scaled cutout start x
cutout_y_start = 0.1458 * 0.75  # Scaled cutout start y
cutout_size = (0.3233 - 0.1767) * 0.75  # Scaled cutout size
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
    .faces(">Z")
    .workplane()
    .moveTo(cutout_x_start - length/2, cutout_y_start - width/2)
    .rect(cutout_size, cutout_size)
    .cutThruAll()
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.0121))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.cq.exporters.export(assembly,
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_909.stl