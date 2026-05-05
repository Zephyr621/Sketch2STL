import cadquery as cq
# --- Part 1: Cube with Cutout ---
part_1_length = 0.5733 * 0.75  # Scaled length
part_1_width = 0.75 * 0.75   # Scaled width
part_1_height = 0.7037
cutout_x_start = 0.1749 * 0.75
cutout_y_start = 0.2785 * 0.75
cutout_x_end = 0.4773 * 0.75
cutout_y_end = 0.4702 * 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
    .faces(">Z").workplane()
    .moveTo(cutout_x_start - part_1_length/2, cutout_y_start - part_1_width/2)
    .rect(cutout_x_end - cutout_x_start, cutout_y_end - cutout_y_start)
    .cutThruAll()
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.7037, 0))
# --- Part 2: Cutout ---
part_2_length = 0.6
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2974.stl