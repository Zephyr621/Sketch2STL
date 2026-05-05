import cadquery as cq
# --- Part 1: Square Plate ---
part_1_size = 0.75 * 0.75  # Sketch size scaled
part_1_height = 0.0114
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_size, part_1_size)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0114, 0))
# --- Part 2: Cube ---
part_2_size = 0.6286 * 0.6286  # Sketch size scaled
part_2_height = 0.0293
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_size, part_2_size)
    .extrude(part_2_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.0114, 0.0293, 0.0114))
# --- Assembly ---
assembly = part_1.union(part_2)
cq.cq.exporters.export({result_var}, "output_3464.stl"output_3464.stl