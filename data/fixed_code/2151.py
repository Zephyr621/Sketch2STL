import cadquery as cq
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_height = 0.0608
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(-part_1_height)
# --- Part 2: Smaller Cylinder on Top ---
part_2_radius = 0.0407 * 0.0814  # Sketch radius scaled
part_2_height = 0.0385
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0.3071, 0.3071, 0.0608))
# --- Assembly ---
assembly = part_1.union(part_2)
# --- Export to STL ---
# --- Export to STL ---
# --- Export to ST
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_2151.stl