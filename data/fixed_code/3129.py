import cadquery as cq
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.0417 * 0.0833  # Sketch radius scaled
part_1_height = 0.1667
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(-part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0.0088, 0.75, 0.0088))
# --- Part 2: Flange ---
part_2_radius = 0.0208 * 0.0417  # Sketch radius scaled
part_2_height = 0.75
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.0144, 0.75, 0.0144))
# --- Part 3: Flange ---
part_3_outer_radius = 0.0208 * 0.0417  # Sketch radius scaled
part_3_inner_radius = 0.0208 * 0.0417
part_3_height = 0.75
part_3 = (
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_3129.stl