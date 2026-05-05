import cadquery as cq
# --- Part 1: Cube with Cutout ---
length = 0.75 * 0.75  # Scaled length
width = 0.50 * 0.75  # Scaled width
height = 0.25
cutout_x1 = 0.125 * 0.75  # Scaled cutout x X
cutout_y1 = 0.125 * 0.75  # Scaled cutout y Y
cutout_x2 = 0.625 * 0.75  # Scaled cutout x 2
cutout_y2 = 0.625 * 0.75  # Scaled cutout y 2
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
    .faces(">Z").workplane()
    .moveTo(cutout_x1 - length/2, cutout_y1 - width/2)
    .lineTo(cutout_x2 - length/2, cutout_y1 - width/2)
    .lineTo(cutout_x2 - length/2, cutout_y2 - width/2)
    .close()
    .cutThruAll()
)
# --- Assembly ---
assembly = part_1
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2222.stl