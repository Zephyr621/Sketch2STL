import cadquery as cq
from cadquery import exporters
# --- Part 1: Cube ---
part_1_length = 0.3454 * 0.3454  # Scaled length
part_1_width = 0.2431 * 0.3454   # Scaled width
part_1_height = 0.152
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0.0984, 0.6322, 0.0948))
# --- Part 2: Cylinder ---
part_2_radius = 0.375 * 0.75  # Scaled radius
part_2_height = 0.0703
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_radius)
    .extrude(-part_2_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0, 0, 0))
# --- Assembly ---
assembly = part_1.union(part_2)
# --- Export to STL ---
cq.exporters.export(assembly
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_179.stl