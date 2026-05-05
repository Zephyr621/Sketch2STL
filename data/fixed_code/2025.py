import cadquery as cq
# --- Part 1: Rectangular Plate ---
length = 0.75 * 0.75  # Scaled length
width = 0.225 * 0.75   # Scaled width
height = 0.0375
hole_radius = 0.0188 * 0.75  # Scaled radius
hole1_x = 0.0625 * 0.75
hole1_y = 0.075 * 0.75
hole2_x = 0.6875 * 0.75
hole2_y = 0.075 * 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
    .faces(">Z").workplane()
    .pushPoints([(hole1_x - length/2, hole1_y - width/2), (hole2_x - length/2, hole2_y - width/2)])
    .hole(2 * hole_radius)
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# --- Final Result ---
result = part_1
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.cq.exporters.export(result
# 导出为STL文件
cq.exporters.export(result, "output_2025.stl