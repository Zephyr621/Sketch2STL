import cadquery as cq
from cadquery import exporters
# --- Part 1: Rectangular Block ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.3125 * 0.75  # Scaled width
part_1_height = 0.1875
part_1 = cq.Workplane("XY").rect(part_1_length, part_1_width).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.1875))
# --- Part 2: Cylinder (Cut) ---
part_2_radius = 0.0312 * 0.2813  # Scaled radius
part_2_depth = 0.0225
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(-part_2_depth)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (1, 0, 0), -90)
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_3547.stl