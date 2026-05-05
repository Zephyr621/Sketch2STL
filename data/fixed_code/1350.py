import cadquery as cq
# --- Part 1: Rectangular Box ---
length = 0.75 * 0.75  # Scaled length
width = 0.25 * 0.75  # Scaled width
height = 0.0625 + 0.0625  # Total height (extrusion in both directions)
inner_offset = 0.0156 * 0.75
# Create the outer rectangle
outer_rect = cq.Workplane("XY").rect(length, width).extrude(height)
# Create the inner rectangle (cutout)
inner_rect = cq.Workplane("XY").rect(length - 2 * inner_offset, width - 2 * inner_offset).extrude(height)
# Subtract the inner rectangle from the outer rectangle to create the box shape
part_1 = outer_rect.cut(inner_rect)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.125))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# --- Final Result ---
result = assembly
cq.
cq.cq.exporters.export({result_var}, "output_1350.stl"output_1350.stl