import cadquery as cq
# --- Part 1: Rectangular Plate ---
part_1_length = 0.5 * 0.5  # Scaled length
part_1_width = 0.4643 * 0.5  # Scaled width
part_1_height = 0.0117 + 0.0117  # Total height from extrusion
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.011))
# --- Part 2: Rectangular Plate ---
part_2_length = 0.5 * 0.5  # Scaled length
part_2_width = 0.75 * 0.5  # Scaled width
part_2_height = 0.0117 + 0.0117  # Total height from extrusion
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_length, part_2_width)
    .extrude(part_2_height)
)
# --- Assembly ---
assembly = part_2.union(part_1)
cq.cq.exporters.export({result_var}, "output_2711.stl"output_2711.stl