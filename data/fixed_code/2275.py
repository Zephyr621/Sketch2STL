import cadquery as cq
# --- Part 1: Rectangular Block ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.375 * 0.75   # Scaled width
part_1_height = 0.0938 + 0.0938
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.1875, 0))
# --- Part 2: Cylindrical Protrusions ---
cylinder_radius = 0.0625 * 0.75  # Scaled radius
cylinder_height = 0.0938 + 0.0938
cylinder_locations = [
    (0.0625 * 0.75, 0.0625 * 0.75),
    (0.6875 * 0.75, 0.0625 * 0.75),
    (0.6875 * 0.75, 0.6875 * 0.75),
]
part_2 = cq.Workplane("XY")
for x, y in cylinder_locations:
    part_2 = part_2.moveTo(x, y).circle(cylinder_radius).extrude(cylinder_height)
# --- Coordinate System Transformation for Part 2 ---
part
# Export
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_2275.stl