import cadquery as cq
# --- Part 1: Rectangular Plate ---
part_1_length = 0.4827 * 0.75  # Scaled length
part_1_width = 0.75 * 0.75  # Scaled width
part_1_height = 0.0344
cutout_x = 0.0479 * 0.75
cutout_y = 0.0479 * 0.75
cutout_length = (0.4827 - 0.0479) * 0.75
cutout_width = (0.7174 - 0.0479) * 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
    .faces(">Z").workplane()
    .moveTo(cutout_x - part_1_length/2, cutout_y - part_1_width/2)
    .rect(cutout_length, cutout_width)
    .cutThruAll()
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2917.stl