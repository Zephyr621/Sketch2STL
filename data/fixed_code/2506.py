import cadquery as cq
# --- Part 1: Rectangular Beam ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.4432 * 0.75  # Scaled width
part_1_height = 0.1389
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.1389, 0))
# --- Part 2: Cube ---
part_2_size = 0.4309 * 0.4309  # Scaled size
part_2_depth = 0.2622
part_2 = (
    cq.Workplane("XY")
    .rect(part
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2506.stl