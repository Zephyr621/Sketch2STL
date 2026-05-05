import cadquery as cq
# --- Part 1: Rectangular Block ---
part_1_length = 0.18 * 0.18  # Scaled length
part_1_width = 0.06 * 0.18  # Scaled width
part_1_height = 0.1875 + 0.1875  # Total height from extrusion in both directions
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.375, 0))
# --- Assembly ---
assembly = part_1
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.375, 0))
# --- Export to STL ---
cq.cq.exporters.export({result_var}, "output_3523.stl"output_3523.stl