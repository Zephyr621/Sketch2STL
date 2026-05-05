import cadquery as cq
# --- Part 1: Square Plate ---
plate_length = 0.6868 * 0.75  # Scaled length
plate_width = 0.75 * 0.75  # Scaled width
plate_height = 0.0703
part_1 = (
    cq.Workplane("XY")
    .rect(plate_length, plate_width)
    .extrude(plate_height)
)
# --- Part 2: Circular Hole ---
hole_radius = 0.0117 * 0.0885  # Scaled radius
hole_depth = 0.0703
part_2 = (
    cq.Workplane("XY")
    .circle(hole_radius)
    .extrude(-hole_depth)  # Extrude in the opposite direction for a hole
)
# --- Assembly: Cut the hole from the plate ---
result = part_1.cut(part_2)
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.cq.exporters.export(result,
# 导出为STL文件
cq.exporters.export(result, "output_2831.stl