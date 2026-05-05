import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder ---
part_1_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_height = 0.0225
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Part 2: Square Indentation ---
part_2_width = 0.375 * 0.375  # Sketch width scaled
part_2_height = 0.0112 * 0.375 # Sketch height scaled
part_2_depth = 0.0112 * 2  # Total depth (both directions)
part_2 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(part_2_width, part_2_height)
    .lineTo(part_2_width / 2, part_2_height)
    .lineTo(0, part_2_height)
    .close()
    .extrude(part_2_depth)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0.0638, 0.0638, 0))
# --- Assembly ---
assembly = part_1.union(part_2)
cq.
# --- Final Result ---
result = assembly
cq
# 导出为STL文件
cq.exporters.export(result, "output_2740.stl