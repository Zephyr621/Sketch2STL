import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder ---
part_1_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_height = 0.4288
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.4288, 0))
# --- Part 2: Rectangular Plate ---
part_2_width = 0.0833 * 0.5047  # Sketch width scaled
part_2_length = 0.5047 * 0.5047  # Sketch length scaled
part_2_height = 0.0341
part_2 = cq.Workplane("XY").rect(part_2_width, part_2_length).extrude(part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0.0417, 0.2346, 0.0597))
# --- Part 3: Rectangular Prism ---
part_3_width = 0.0573 * 0.5047  # Sketch width scaled
part_3_length = 0.0833 * 0.5047  # Sketch length
# Export
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_787.stl