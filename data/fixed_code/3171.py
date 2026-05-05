import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder ---
part_1_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_height = 0.0469
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0469, 0))
# --- Part 2: Cut Cylinder ---
part_2_radius = 0.2344 * 0.4688  # Sketch radius scaled
part_2_height = 0.0117
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(-part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.1406, 0, 0.1406))
# --- Part 3: Cut Cylinder ---
part_3_radius = 0.2188 * 0.4687  # Sketch radius scaled
part_3_height = 0.0117
part_3 = cq.Workplane("XY").circle(part_3_radius).extrude(-part_3_height)
# Export
# 定义结果变量
result = part_3
# 导出为STL文件
cq.exporters.export(result, "output_3171.stl