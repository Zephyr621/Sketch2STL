import cadquery as cq
from cadquery.vis import show
# --- Part 1: Rectangular Block ---
part_1_length = 0.7429 * 0.7429  # Scaled length
part_1_width = 0.314 * 0.7429   # Scaled width
part_1_height = 0.211
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.0484, 0.0484, 0))
# --- Part 2: Cylinder ---
part_2_radius = 0.2054 * 0.411  # Scaled radius
part_2_height = 0.212
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_radius)
    .extrude(part_2_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0.5179, 0.5567, 0.213))
# --- Assembly ---
assembly = part_1.union(part_2)
cq.
# --- Final Result ---
result = assembly
cq.cq.exporters.export(result
# 导出为STL文件
cq.exporters.export(result, "output_1318.stl