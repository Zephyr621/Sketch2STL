import cadquery as cq
# --- Part 1: Rectangular Prism with Triangular Cutout ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.1753 * 0.75  # Scaled width
part_1_height = 0.0536
cutout_x = 0.2724 * 0.75
cutout_y = 0.1299 * 0.75
cutout_z = 0.0536
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)  # Extrude in the opposite direction for cutting
)
cutout = (
    cq.Workplane("XY")
    .moveTo(0, 0.0732 * 0.75)
    .lineTo(0.6027 * 0.75, 0.0732 * 0.75)
    .lineTo(0.6954 * 0.75, 0.0732 * 0.75)
    .lineTo(0.6837 * 0.75, 0.0732 * 0.75)
    .lineTo(0.75 * 0.75, 0.0732 * 0.75)
    .lineTo(0.75 * 0.75, 0.
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2474.stl