import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cube ---
part_1_size = 0.3 * 0.3  # Sketch size scaled
part_1_height = 0.25
part_1 = cq.Workplane("XY").box(part_1_size, part_1_size, part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2: Cylinder ---
part_2_radius = 0.075 * 0.15  # Sketch radius scaled
part_2_height = 0.625
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.225, 0.625, 0.225))
# --- Assembly ---
assembly = part_1.union(part_2)
cq.
cq.
cq.exp
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_893.stl