import cadquery as cq
# --- Part 1: Rectangular Box ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.45 * 0.75  # Scaled width
part_1_height = 0.15
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Part 2: Cylinder ---
part_2_radius = 0.1125 * 0.225  # Scaled radius
part_2_height = 0.3
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_radius)
    .extrude(-part_2_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0.1875, 0.1875, part_1_height))
# --- Assembly ---
assembly = part_1.union(part_2)
cq.
# --- Export to STL ---
cq.
# --- Final Result ---
result = assembly
cq.cq.exporters.export(result,
# 导出为STL文件
cq.exporters.export(result, "output_945.stl