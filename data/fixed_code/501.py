import cadquery as cq
# --- Part 1: Cube with Hole ---
part_1_size = 0.75 * 0.75  # Scaled size
part_1_hole_offset = 0.0625 * 0.75  # Scaled offset
part_1_height = 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_size, part_1_size)
    .extrude(-part_1_height)  # Extrude downwards for cut
    .faces(">Z")
    .workplane()
    .rect(part_1_size - 2 * part_1_hole_offset, part_1_size - 2 * part_1_hole_offset)
    .cutThruAll()
)
# --- Part 2: Rectangular Prism (Cutout) ---
part_2_width = 0.125 * 0.375  # Scaled width
part_2_length = 0.375 * 0.375  # Scaled length
part_2_depth = 0.25
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_width, part_2_length)
    .extrude(-part_2
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_501.stl