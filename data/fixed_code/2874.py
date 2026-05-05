import cadquery as cq
# --- Part 1: L-shaped CAD Model ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.0461 * 0.0461, 0.0)
    .lineTo(0.0461 * 0.0461, 0.0064 * 0.0461)
    .lineTo(0.0032 * 0.0461, 0.0064 * 0.0461)
    .lineTo(0.0032 * 0.0461, 0.0187 * 0.0461)
    .lineTo(0.0, 0.0187 * 0.0461)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(-0.75)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
#part_1 = part_1.translate((0, 0, 0)) # Translation is zero, so no need to translate
# --- Assembly ---
assembly = part_1
# Export to STL
cq.cq.exporters.export({result_var}, "output_2874.stl"output_2874.stl