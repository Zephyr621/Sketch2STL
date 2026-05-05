import cadquery as cq
from cadquery import exporters
# --- Part 1: Base Cylinder ---
part_1_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_height = 0.2083
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Part 2: Top Cylinder ---
part_2_radius = 0.3214 * 0.6571  # Sketch radius scaled
part_2_height = 0.2917
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0.1167, 0.1167, 0.2083))
# --- Assembly ---
assembly = part_1.union(part_2)
# --- Export to STL ---
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_267.stl