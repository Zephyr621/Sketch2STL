import cadquery as cq
# --- Part 1: Rectangular Plate ---
part_1_length = 0.2344 * 0.6562  # Scaled length
part_1_width = 0.6562 * 0.6562  # Scaled width
part_1_height = 0.0288
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.0484, 0.0484, 0))
# --- Part 2: Central Hole ---
part_2_radius = 0.375 * 0.75  # Scaled radius
part_2_depth = 0.0577
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_radius)
    .extrude(-part_2_depth)  # Extrude in the opposite direction for cutting
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0, 0, part_1_height))
# --- Assembly: Cut the hole from the plate ---
assembly
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3461.stl