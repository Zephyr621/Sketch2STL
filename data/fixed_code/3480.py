import cadquery as cq
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.1607 * 0.3214  # Sketch radius scaled
part_1_height = 0.7143
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(-part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Part 2: Rectangular Top ---
part_2_length = 0.4286 * 0.4286  # Sketch length scaled
part_2_width = 0.5357 * 0.4286  # Sketch width scaled
part_2_height = 0.0429
part_2 = cq.Workplane("XY").rect(part_2_length, part_2_width).extrude(part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.1607, 0, 0.1607))
# --- Assembly ---
assembly = part_1.union(part_2)
# --- Export to STL ---
cq.exporters.export(assembly,
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_3480.stl