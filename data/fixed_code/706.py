import cadquery as cq
from math import radians
# --- Part 1: Rectangular Block ---
part_1_length = 0.0533 * 0.6818  # Scaled length
part_1_width = 0.6818 * 0.6818  # Scaled width
part_1_height = 0.2134
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.0317, 0.0727, 0))
# --- Part 2: Cylinder ---
part_2_radius = 0.0533 * 0.1154  # Scaled radius
part_2_height = 0.2058
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_radius)
    .extrude(part_2_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), 180)
part_2 = part_2.translate((0.0859, 0.5337, 0))
# --- Assembly ---
assembly = part_1.union(part_2)
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_706.stl