import cadquery as cq
from cadquery import exporters
# --- Part 1: Cube ---
part_1_length = 0.6562 * 0.75  # Sketch length scaled
part_1_width = 0.75 * 0.75  # Sketch width scaled
part_1_height = 0.3175
part_1 = cq.Workplane("XY").rect(part_1_length, part_1_width).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.3175, 0))
# --- Part 2: Cylinder ---
part_2_radius = 0.3255 * 0.6562  # Sketch radius scaled
part_2_height = 0.5185
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(-part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), 180)
part_2 = part_2.translate((0.0972, 0.6484, 0.2531))
# --- Assembly ---
assembly = part_1.union(part_2)
# --- Export to STL
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_2359.stl