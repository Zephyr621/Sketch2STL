import cadquery as cq
# --- Part 1: Cube with Cut-off ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.75 * 0.75   # Scaled width
part_1_height = 0.1875
cutout_offset = 0.0625 * 0.75  # Scaled offset
cutout_size = (0.375 - 0.0625) * 0.75  # Scaled size
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
part_1 = part_1.translate((0, 0.1875, 0))
# --- Part 2: Rectangular Prism with Corner Cutout ---
part_2_length = 0.375 * 0.375  # Scaled length
part_2_width = 0.3725 * 0.375   # Scaled width
part_2_height = 0.001
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2576.stl