import cadquery as cq
from math import radians
# --- Part 1: Cylinder ---
part_1_radius = 0.0112 * 0.0311  # Sketch radius scaled
part_1_height = 0.75
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(-part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.0106, 0.0106, 0))
# --- Part 2: Rectangular Block ---
block_length = 0.0015 * 0.0298
block_width = 0.0298 * 0.0298
block_height = 0.0717
part_2 = (
    cq.Workplane("XY")
    .rect(block_length, block_width)
    .extrude(block_height)
)
# --- Assembly ---
assembly = part_2.union(part_1)
cq.
# --- Export to STL ---
cq.
cq.cq.exporters.export(assembly
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_1499.stl