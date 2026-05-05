import cadquery as cq
# --- Part 1: Cylinder with Rectangular Section ---
part_1_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_height = 0.3125
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# Create the cutout sketch
cutout_width = (0.3562 - 0.375) * 0.75
cutout_height = (0.25 - 0.5) * 0.75
cutout_x_offset = 0.5 * 0.75
cutout_y_offset = 0.125 * 0.75
cutout = (
    cq.Workplane("XY")
    .moveTo(cutout_x_offset, cutout_y_offset)
    .lineTo(cutout_width, cutout_y_offset)
    .lineTo(cutout_width, cutout_y_offset + cutout_height)
    .lineTo(cutout_x_offset, cutout_y_offset + cutout_height)
    .close()
    .extrude(part_1_height + 0.1)  # Extrude slightly more than the main part
)
# Subtract the cutout from the main body
result = part_1.cut
# Export
# 导出为STL文件
cq.exporters.export(result, "output_618.stl