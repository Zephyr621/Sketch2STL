import cadquery as cq
# --- Part 1: Square Plate with Hole ---
plate_size = 0.75 * 0.75  # Scaled plate size
hole_radius = 0.0625 * 0.75  # Scaled hole radius
plate_thickness = 0.021
wp = cq.Workplane("XY").rect(plate_size, plate_size).extrude(plate_thickness)
part_1 = wp.faces(">Z").workplane().circle(hole_radius).cutThruAll()
# --- Final Result ---
result = part_1
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.exp
# 导出为STL文件
cq.exporters.export(result, "output_1579.stl