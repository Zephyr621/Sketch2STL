import cadquery as cq
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_height = 0.1765
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(-part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.1765))
# --- Part 2: Cut Feature ---
part_2_radius = 0.3562 * 0.7043  # Sketch radius scaled
part_2_depth = 0.0469
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(-part_2_depth)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), 180)
part_2 = part_2.translate((0.0156, 0.6322, 0.1765))
# --- Assembly ---
assembly = part_1.cut(part_2)
# --- Export to STL ---
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_2108.stl