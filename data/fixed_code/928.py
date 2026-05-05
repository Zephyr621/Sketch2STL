import cadquery as cq
# --- Parameters from JSON ---
outer_width = 0.75 * 0.75  # Scaled
inner_width = 0.5357 * 0.75  # Scaled
inner_height = 0.4286 * 0.75  # Scaled
hole_radius = 0.0614 * 0.75  # Scaled
hole_x = 0.1832 * 0.75  # Scaled
hole_y = 0.3409 * 0.75  # Scaled
extrude_depth = 0.1172
# --- Create the base rectangular block ---
base_block = (
    cq.Workplane("XY")
    .rect(outer_width, outer_height)
    .extrude(extrude_depth)
)
# --- Cut the inner rectangle ---
inner_rect = (
    cq.Workplane("XY")
    .rect(inner_width - 2 * hole_x, inner_height - 2 * hole_y)
    .extrude(extrude_depth + 0.1)  # Extrude slightly more to ensure complete cut
)
result = base_block.cut(inner_rect)
cq.
# --- Export to ST
# 导出为STL文件
cq.exporters.export(result, "output_928.stl