import cadquery as cq
# --- Part 1: Rectangular Prism ---
part_1_width = 0.3798 * 0.75  # Sketch width scaled
part_1_height = 0.3586 * 0.75 # Sketch height scaled
part_1_depth = 0.0799
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(part_1_width, 0)
    .lineTo(part_1_width, part_1_height)
    .lineTo(0, part_1_height)
    .close()
    .extrude(part_1_depth)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0799, 0))
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.cq.exporters.export({result_var}, "output_2544.stl"output_2544.stl