import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder ---
part_1_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_height = 0.2871
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.2871, 0))
# --- Part 2: Small Cylinder ---
part_2_radius = 0.3455 * 0.6818  # Sketch radius scaled
part_2_height = 0.0577
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(-part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.0295, 0, 0.0295))
# --- Assembly ---
assembly = part_1.union(part_2)
cq.
cq
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_427.stl