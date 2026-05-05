import cadquery as cq
# --- Part 1: Rectangular Block ---
outer_width = 0.75 * 0.75  # Scaled width
outer_length = 0.375 * 0.75  # Scaled length
inner_offset = 0.075 * 0.75  # Scaled offset for inner rectangle
height = 0.1125
part_1 = (
    cq.Workplane("XY")
    .rect(outer_width, outer_length)
    .extrude(height)
    .faces(">Z")
    .workplane()
    .rect(outer_width - 2 * inner_offset, outer_length - 2 * inner_offset)
    .cutThruAll()
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.1125, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# --- Export to STL ---
cq.
# Export to STL
cq.cq.exporters.export({result_var}, "output_2644.stl"output_2644.stl