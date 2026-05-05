import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cube ---
part_1_size = 0.75 * 0.75  # Sketch size scaled
part_1_height = 0.75
part_1 = cq.Workplane("XY").rect(part_1_size, part_1_size).extrude(-part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Part 2: Cylinder (Hole) ---
part_2_radius = 0.0937 * 0.1988  # Sketch radius scaled
part_2_height = 0.75
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(-part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.1833, 0, 0.1833))
# --- Assembly: Cut the hole from the cube ---
assembly = part_1.cut(part_2)
cq.
# --- Export to ST
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_831.stl