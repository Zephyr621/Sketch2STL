import cadquery as cq
# --- Part 1: Rectangular Block with Circular Hole ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.2625 * 0.75  # Scaled width
part_1_height = 0.75
hole_center_x = 0.375 * 0.75  # Scaled center x
hole_center_y = 0.1312 * 0.75  # Scaled center y
hole_radius = 0.0469 * 0.75  # Scaled radius
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
    .faces(">Z")
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2453.stl