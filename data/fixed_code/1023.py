import cadquery as cq
# --- Part 1: Rectangular Prism with Cutout ---
length = 0.3125 * 0.75  # Scaled length
width = 0.1607 * 0.75  # Scaled width
height = 0.75
cutout_x_start = 0.0156 * 0.75  # Scaled cutout start x
cutout_y_start = 0.0094 * 0.75  # Scaled cutout end y
cutout_width = (0.4687 - 0.0156) * 0.75  # Scaled cutout width
cutout_height = (0.2569 - 0.0094) * 0.75  # Scaled cutout height
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
    .faces(">Z").workplane()
    .moveTo(cutout_x_start - length/2, cutout_y_start - width/2)
    .rect(cutout_width, cutout_height)
    .cutThruAll()
)
# --- Assembly ---
assembly = part_1
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1023.stl