import cadquery as cq
from math import radians
# --- Part 1: Square Plate ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.75 * 0.75  # Scaled width
part_1_height = 0.0094
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Part 2: Cylinder (Hole) ---
part_2_radius = 0.2297 * 0.4583  # Scaled radius
part_2_depth = 0.2917
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_radius)
    .extrude(-part_2_depth)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), 180)
part_2 = part_2.translate((0.1167, 0.5366, 0))
# --- Part 3: Cube with Rounded Edges ---
part_3_size = 0.375 * 0.375
part_3_depth = 0.0536
part_3 = (
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2893.stl