import cadquery as cq
# --- Part 1: Rectangular Plate ---
plate_length = 0.625 * 0.75  # Scaled length
plate_width = 0.75 * 0.75  # Scaled width
plate_height = 0.0625
part_1 = cq.Workplane("XY").rect(plate_length, plate_width).extrude(plate_height)
# --- Part 2: Holes ---
hole_radius = 0.0062 * 0.65  # Scaled radius
hole_depth = 0.0625
# Hole centers (scaled and translated)
hole_centers = [
    (0.0312 * 0.75 - plate_length/2, 0.0147 * 0.75 - plate_width/2),
    (0.0288 * 0.75 - plate_length/2, 0.0147 * 0.75 - plate_width/2),
    (0.7222 * 0.75 - plate_length/2, 0.0147 * 0.75 - plate_width/2),
    (0.7222 * 0.75 - plate_length/2, 0.7211 * 0.75 - plate_width/2),
]
# Create holes
for x, y in hole_centers:
    part_1 = part_1.faces(">Z").workplane().pushPoints([(x, y)]).hole(2 * hole_radius)
# --- Assembly ---
assembly = part_1
# --- Export to STL ---
cq.
# Export
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_637.stl