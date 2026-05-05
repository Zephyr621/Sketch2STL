import cadquery as cq
# --- Part 1: Rectangular Plate ---
part_1_length = 0.2303 * 0.3937  # Scaled length
part_1_width = 0.3937 * 0.3937  # Scaled width
part_1_height = 0.0161
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.0519, 0.0058, 0))
# --- Part 2: Cylinder (Join) ---
part_2_radius = 0.3594 * 0.7125  # Scaled radius
part_2_height = 0.0702
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_radius)
    .extrude(-part_2_height)  # Extrude downwards
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0.0519, 0.0058, 0.0161))
# --- Assembly ---
assembly = part_1.union(part_2)
cq.cq.exporters.export({result_var}, "output_2938.stl"output_2938.stl