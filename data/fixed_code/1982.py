import cadquery as cq
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.2679 * 0.5172  # Sketch radius scaled
part_1_height = 0.1034
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.1167, 0.1167, 0))
# --- Part 2: Hole ---
part_2_radius = 0.2083 * 0.4167  # Sketch radius scaled
part_2_height = 0.0568
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(-part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (1, 0, 0), -90)
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.5172, 0.0117, 0.1667))
# --- Assembly ---
assembly = part_1.cut(part_2)
# --- Export to
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_1982.stl