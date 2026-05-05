import cadquery as cq
from cadquery import exporters
# --- Part 1: Base ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.625 * 0.75  # Scaled width
part_1_height = 0.5
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.5, 0))
# --- Part 2: Hole in Base ---
hole_radius = 0.0625 * 0.125  # Scaled radius
hole_depth = 0.25
part_2 = (
    cq.Workplane("XY")
    .circle(hole_radius)
    .extrude(-hole_depth)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1252.stl