import cadquery as cq
# --- Part 1: Rectangular Plate ---
plate_length = 0.75 * 0.75  # Scaled length
plate_width = 0.5098 * 0.75  # Scaled width
plate_height = 0.0395
part_1 = cq.Workplane("XY").rect(plate_length, plate_width).extrude(plate_height)
# --- Part 2: Holes ---
hole_radius = 0.0208 * 0.6507  # Scaled radius
hole_depth = 0.0395
hole_centers = [
    (0.0208 * 0.6507, 0.2188 * 0.6507),
    (0.0208 * 0.6507, 0.3748 * 0.6507),
    (0.4262 * 0.6507, 0.0208 * 0.6507),
    (0.4262 * 0.6507, 0.3748 * 0.6507),
]
for x, y in hole_centers:
    part_1 = part_1.faces(">Z").workplane().pushPoints([(x - plate_length/2, y - plate_width/2)]).hole(2 * hole_radius)
# --- Assembly: Cut Holes from Plate ---
result = part_1
# --- Export to STL ---
cq.
# --- Export to ST
# 导出为STL文件
cq.exporters.export(result, "output_1858.stl