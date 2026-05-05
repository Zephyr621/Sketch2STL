import cadquery as cq
# --- Part 1: Rectangular Plate ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.375 * 0.75  # Scaled width
part_1_height = 0.0234
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Part 2: Groove Cutout ---
part_2_radius = 0.0117 * 0.7031  # Scaled radius
part_2_depth = 0.0234
part_2 = (
    cq.Workplane("XY")
    .moveTo(0.0117 * 0.7031, 0.0117 * 0.7031)  # Scaled center
    .circle(part_2_radius)
    .extrude(-part_2_depth)  # Extrude downwards for cutting
)
# --- Assembly: Cut the groove from the plate ---
assembly = part_1.cut(part_2.translate((0.0117, 0.0117, part_1_height)))
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_409.stl