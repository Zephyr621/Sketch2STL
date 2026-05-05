import cadquery as cq
# --- Part 1: Square Plate ---
plate_length = 0.75 * 0.75  # Scaled length
plate_width = 0.75 * 0.75  # Scaled width
plate_height = 0.0469
# Hole parameters (scaled)
hole_center_offset = 0.0105 * 0.75
hole_radius = 0.0058 * 0.75
# Create the base square plate
plate = cq.Workplane("XY").rect(plate_length, plate_width).extrude(plate_height)
# Subtract corner holes
hole_locations = [
    (hole_center_offset - plate_length / 2, hole_center_offset - plate_width / 2),
    (hole_center_offset - plate_length / 2, plate_width / 2 - hole_center_offset),
    (plate_length / 2 - hole_center_offset, hole_center_offset - plate_width / 2),
]
for x, y in hole_locations:
    plate = plate.faces(">Z").workplane().pushPoints([(x, y)]).hole(2 * hole_radius)
# Export the result to a STL file
cq.
# --- Final Result ---
result = plate
cq.cq.exporters.export(result
# 导出为STL文件
cq.exporters.export(result, "output_2801.stl