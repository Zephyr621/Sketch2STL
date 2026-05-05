import cadquery as cq
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_height = 0.075
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(-part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Part 2: Cut ---
part_2_radius = 0.0938 * 0.1875  # Sketch radius scaled
part_2_depth = 0.375
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(-part_2_depth)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.2812, 0, 0.2812))
# --- Assembly ---
assembly = part_1.cut(part_2)
# --- Export to STL ---
exp
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_1766.stl