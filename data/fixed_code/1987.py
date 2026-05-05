import cadquery as cq
from cadquery import exporters
# --- Part 1: Cube ---
part_1_size = 0.75 * 0.75  # Sketch size scaled
part_1_height = 0.1271
part_1 = cq.Workplane("XY").box(part_1_size, part_1_size, part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.1271, 0))
# --- Part 2: Hole ---
part_2_radius = 0.3562 * 0.7125  # Sketch radius scaled
part_2_depth = 0.0506
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(-part_2_depth)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.0147, 0, 0.0147))
# --- Part 3: Hole 2 ---
part_3_radius = 0.0147 * 0.7125  # Sketch radius scaled
part_3_depth = 0.1299
part_3 = cq.Workplane("XY
# 定义结果变量
result = part_3
# 导出为STL文件
cq.exporters.export(result, "output_1987.stl