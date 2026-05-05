import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder ---
part_1_radius = 0.1125 * 0.225  # Sketch radius scaled
part_1_height = 0.6
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(-part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.0575, 0.0575, 0.6))
# --- Part 2: Smaller Cylinder on Top ---
part_2_radius = 0.1125 * 0.225  # Sketch radius scaled
part_2_height = 0.6
part_2 = (
    cq.Workplane("XY")
    .moveTo(0.1125 * 0.225, 0.1125 * 0.225)  # Translation Vector scaled
    .circle(part_2_radius)
    .extrude(part_2_height)
)
# --- Assembly ---
assembly = part_2.union(part_1)
cq.
# --- Final Result ---
result = assembly
cq.
cq.
cq.
cq.
# 导出为STL文件
cq.exporters.export(result, "output_1370.stl