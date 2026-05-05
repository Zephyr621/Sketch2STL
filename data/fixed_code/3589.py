import cadquery as cq
from cadquery import exporters
# --- Part 1: Cylinder with Hole ---
part_1_radius = 0.2344 * 0.4688  # Sketch radius scaled
part_1_height = 0.1016
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2: Cut Cylinder ---
part_2_radius = 0.2062 * 0.4375  # Sketch radius scaled
part_2_height = 0.0412
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(-part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.1172, 0, 0.1172))
# --- Assembly ---
assembly = part_1.cut(part_2)
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_3589.stl