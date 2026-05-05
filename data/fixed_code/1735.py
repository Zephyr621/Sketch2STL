import cadquery as cq
from cadquery.vis import show
# --- Part 1: Rectangular Plate ---
length = 0.75 * 0.75  # Scaled length
width = 0.5172 * 0.75  # Scaled width
height = 0.0049
# Hole parameters (scaled)
hole1_center = (0.0938 * 0.75 - length/2, 0.2751 * 0.75 - width/2)
hole2_center = (0.6562 * 0.75 - length/2, 0.2751 * 0.75 - width/2)
hole_radius = 0.0099 * 0.75
# Create the base rectangular plate
plate = cq.Workplane("XY").rect(length, width).extrude(height)
# Add holes
plate = (
    plate.faces(">Z")
    .workplane()
    .pushPoints([hole1_center, hole2_center])
    .hole(hole_radius * 2)
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# --- Final Result ---
result = plate
cq.
# Export to STL
cq.
# Export
# 导出为STL文件
cq.exporters.export(result, "output_1735.stl