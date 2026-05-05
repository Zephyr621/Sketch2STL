import cadquery as cq
# --- Part 1: Rectangular Object with Hollow Center ---
outer_width = 0.75 * 0.75  # Scaled width
outer_height = 0.5427 * 0.75  # Scaled height
inner_offset = 0.0405 * 0.75  # Scaled offset for inner rectangle
extrude_depth = 0.0086  # Total extrusion depth (towards + opposite)
part_1 = (
    cq.Workplane("XY")
    .rect(outer_width, outer_height)
    .extrude(extrude_depth)
    .cut(cq.Workplane("XY").rect(outer_width - 2 * inner_offset, outer_height - 2 * inner_offset).extrude(extrude_depth))
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.0086))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# --- Export to STL ---
cq.
# --- Final Result ---
result = assembly
# Export to STL
cq.
# 导出为STL文件
cq.exporters.export(result, "output_265.stl