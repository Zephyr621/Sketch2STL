import cadquery as cq
from cadquery import exporters
# --- Part 1: Rectangular Bar ---
part_1_length = 0.7023 * 0.7023  # Scaled length
part_1_width = 0.7125 * 0.7023   # Scaled width
part_1_height = 0.0562
part_1 = cq.Workplane("XY").rect(part_1_length, part_1_width).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0.0187, 0.0562, 0))
# --- Part 2: Cylinder (Hole) ---
part_2_radius = 0.0176 * 0.0274  # Scaled radius
part_2_depth = 0.0562
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(-part_2_depth)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (1, 0, 0), 180)
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.7023, 0.0562, 0))
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_1103.stl