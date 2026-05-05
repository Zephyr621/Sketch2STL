import cadquery as cq
# --- Part 1: Cube with Hole ---
part_1_size = 0.75 * 0.75  # Scaled size
part_1_hole_x_offset = 0.0938 * 0.75  # Scaled offset
part_1_hole_y_offset = 0.6562 * 0.75  # Scaled offset
part_1_height = 0.375
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_size, part_1_size)
    .extrude(part_1_height)
    .faces(">Z")
    .workplane()
    .rect(part_1_size - 2 * part_1_hole_x_offset, part_1_size - 2 * part_1_hole_y_offset)
    .cutThruAll()
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.375, 0))
# --- Part 2: Cylinder Cutout ---
part_2_radius = 0.2812 * 0.5625  # Scaled radius
part_2_depth = 0.1875
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1705.stl