import cadquery as cq
# --- Part 1: Rectangular Prism ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.3125 * 0.75  # Scaled width
part_1_height = 0.0938
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Part 2: Cylinder ---
part_2_radius = 0.125 * 0.3125  # Scaled radius
part_2_height = 0.25
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_radius)
    .extrude(-part_2_height)  # Extrude in the opposite direction for cutting
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0.125, 0.125, 0.0938))
# --- Assembly ---
assembly = part_1.union(part_2)
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1951.stl