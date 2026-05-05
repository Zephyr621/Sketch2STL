import cadquery as cq
# --- Part 1: Rectangular Block ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.2753 * 0.75  # Scaled width
part_1_height = 0.075
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.075, 0))
# --- Part 2: Cylinder ---
part_2_radius = 0.0278 * 0.0481  # Scaled radius
part_2_height = 0.0162
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_radius)
    .extrude(-
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2058.stl