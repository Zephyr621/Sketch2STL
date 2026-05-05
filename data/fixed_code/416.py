import cadquery as cq
# --- Part 1: Base Cylinder ---
part_1_radius = 0.015 * 0.375  # Sketch radius scaled
part_1_height = 0.0188
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2: Top Rectangular Prism ---
part_2_width = 0.375 * 0.375  # Sketch width scaled
part_2_height = 0.3675
part_2_depth = 0.0475
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_width, part_2_height)
    .extrude(-part_2_depth)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (1, 0, 0), 180)
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 =
# Export
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_416.stl