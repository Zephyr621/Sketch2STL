import cadquery as cq
from math import radians
# --- Part 1: Cube ---
part_1_width = 0.75 * 0.75  # Sketch width scaled
part_1_height = 0.7338 * 0.75 # Sketch height scaled
part_1_depth = 0.0131
part_1 = cq.Workplane("XY").rect(part_1_width, part_1_height).extrude(part_1_depth)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0131, 0))
# --- Part 2: Cutout Cube ---
part_2_length = 0.75 * 0.75  # Sketch length scaled
part_2_width = 0.7265 * 0.75  # Sketch width scaled
part_2_height =
# Export
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_2542.stl