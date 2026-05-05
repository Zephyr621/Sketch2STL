import cadquery as cq
from cadquery import exporters
# --- Part 1: Rectangular Box ---
part_1_length = 0.1562 * 0.1562  # Scaled length
part_1_width = 0.1467 * 0.1562  # Scaled width
part_1_height = 0.2449
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (1, 0, 0), -90)
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
# --- Part 2: Cylinder ---
part_2_radius = 0.2344 * 0.7083  # Scaled radius
part_2_height = 0.3789
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_radius)
    .extrude(part_2_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0.0033, 0.0104, 0.2885))
# --- Assembly ---
assembly = part_1.union
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1216.stl