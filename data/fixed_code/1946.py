import cadquery as cq
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_height = 0.1201
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(-part_1_height)
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Part 2: Cylinder ---
part_2_radius = 0.1572 * 0.3287  # Sketch radius scaled
part_2_height = 0.331
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(-part_2_height)
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.3188, 0, 0.3188))
# --- Part 3: Cylinder ---
part_3_radius = 0.0804 * 0.1607  # Sketch radius scaled
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_1946.stl