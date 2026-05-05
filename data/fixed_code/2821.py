import cadquery as cq
# --- Part 1: Rectangular Block ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.25 * 0.75   # Scaled width
part_1_height = 0.1261
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0.0469, 0))
# --- Part 2: Cube ---
part_2_size = 0.75 * 0.75  # Scaled size
part_2_height = 0.0615
part_2 = cq.Workplane("XY").box(part_2_size, part_2_size, part_2_height)
# --- Assembly ---
assembly = part_1.union(part_2)
cq.cq.exporters.export({result_var}, "output_2821.stl"output_2821.stl