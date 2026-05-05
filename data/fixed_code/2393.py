import cadquery as cq
# --- Part 1: Rectangular Plate ---
length = 0.75 * 0.75  # Scaled length
width = 0.3533 * 0.75  # Scaled width
height = 0.0316
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
)
# Cut out the cutout
cutout_x_start = 0.1759 * 0.75
cutout_y_start = 0.1759 * 0.75
cutout_width = (0.6718 - 0.1759) * 0.75
cutout_height = (0.2545 - 0.1759) * 0.75
part_1 = (
    part_1.faces(">Z")
    .workplane()
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
cq.exporters
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2393.stl