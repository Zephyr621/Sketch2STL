import cadquery as cq
# --- Part 1: Rectangular Box ---
part_1_length = 0.625 * 0.625  # Scaled length
part_1_width = 0.5 * 0.625  # Scaled width
part_1_height = 0.25
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.125, 0.125, 0))
# --- Part 2: Cylinder ---
part_2_radius = 0.0625 * 0.125  # Scaled radius
part_2_height = 0.75
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_radius)
    .extrude(part_2_height)
)
# --- Assembly ---
assembly = part_2.union(part_1)
cq.
cq.
cq.
cq.exporters
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3245.stl