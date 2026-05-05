import cadquery as cq
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.0647 * 0.1211  # Sketch radius scaled
part_1_height = 0.75
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(-part_1_height)
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Part 2: Cube ---
part_2_size = 0.0555 * 0.0555  # Sketch size scaled
part_2_height = 0.0804
part_2 = cq.Workplane("XY").rect(part_2_size, part_2_size).extrude(-part_2_height)
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.2786, 0, 0.2786))
# --- Part 3: Cylinder Cutout ---
part_3_radius = 0.0401 * 0.0938  # Sketch radius scaled
part_
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_3200.stl