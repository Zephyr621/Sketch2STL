import cadquery as cq
from cadquery import exporters
# --- Part 1: Cube ---
part_1_length = 0.181 * 0.181  # Sketch length scaled
part_1_width = 0.304 * 0.181  # Sketch width scaled
part_1_height = 0.3313
part_1 = cq.Workplane("XY").rect(part_1_length, part_1_width).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.3094, 0))
# --- Part 2: Cylinder (Hole) ---
part_2_radius = 0.0937 * 0.1875  # Sketch radius scaled
part_2_depth = 0.3444
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(-part_2_depth)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.0763, 0, 0.0763))
# --- Part 3: Rectangular Pri
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_2752.stl