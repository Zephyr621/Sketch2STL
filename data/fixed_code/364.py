import cadquery as cq
# --- Part 1: Rectangular Box ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.2812 * 0.75  # Scaled width
part_1_height = 0.5625
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.375))
# --- Part 2: Cutout ---
cutout_length = 0.7125 * 0.7125  # Scaled length
cutout_width = 0.2917 * 0.7125  # Scaled width
cutout_depth = 0.1875
cutout = (
    cq.Workplane("XY")
    .rect(cutout_length, cutout_width)
    .extrude(-cutout_depth)  # Extrude in the opposite direction for cutting
)
# --- Assembly: Cut Part 2 from Part 1 ---
assembly = part_1.cut(cutout)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_364.stl