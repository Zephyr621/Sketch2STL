import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cube ---
part_1_size = 0.75 * 0.75  # Sketch size scaled
part_1_height = 0.1875 + 0.1875
part_1 = cq.Workplane("XY").box(part_1_size, part_1_size, part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.375, 0))
# --- Part 2: Cylinder ---
part_2_radius = 0.0188 * 0.0262  # Sketch radius scaled
part_2_height = 0.0563 + 0.0563
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.0094, 0.0938, 0.0094))
# --- Part 3: Cylinder ---
part_3_radius = 0.013 * 0.026  # Sketch radius scaled
part_3_height = 0.0563 + 0.0563
part_3 = cq.Workplane("XY").circle(part_3_radius).extrude(part_3_height)
# Export
# 定义结果变量
result = part_3
# 导出为STL文件
cq.exporters.export(result, "output_2358.stl