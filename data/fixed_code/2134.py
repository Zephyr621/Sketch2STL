import cadquery as cq
from cadquery import exporters
# --- Part 1: Square Base ---
part_1_size = 0.4286 * 0.4286  # Sketch size scaled
part_1_height = 0.2143
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_size, part_1_size)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2: Cylinder ---
part_2_radius = 0.1339 * 0.2679  # Sketch radius scaled
part_2_height = 0.75
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_radius)
    .extrude(-part_2_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (1, 0, 0), 90)
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0, 0.75, 0))
# --- Assembly
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2134.stl