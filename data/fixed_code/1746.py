import cadquery as cq
# --- Part 1: Base Rectangular Prism with Cutout ---
part_1_length = 0.5 * 0.75  # Scaled length
part_1_width = 0.75 * 0.75  # Scaled width
part_1_height = 0.5
cutout_x_start = 0.125 * 0.75
cutout_y_start = 0.25 * 0.75
cutout_size = (0.375 - 0.125) * 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
    .faces(">Z")
    .workplane()
    .rect(cutout_size, cutout_size)
    .cutThruAll()
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.5, 0))
# --- Part 2: Cutout ---
part_2_length = 0.25 * 0.625  # Scaled length
part_2_width = 0.625 * 0.625  # Scaled width
part_2_height = 0.25
cutout_x_end = 0.125 * 0
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1746.stl