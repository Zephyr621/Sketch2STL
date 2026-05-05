import cadquery as cq
from cadquery.vis import show
# --- Parameters from JSON ---
length = 0.75 * 0.75  # Scaled length
width = 0.375 * 0.75  # Scaled width
height = 0.0225
hole_radius = 0.0312 * 0.75  # Scaled hole radius
corner_radius = 0.125 * 0.75  # Scaled corner radius
# Hole centers (scaled)
hole_centers = [
    (0.125 * 0.75 - length / 2 + corner_radius, 0),  # Bottom Left
    (0.625 * 0.75 - length / 2 + corner_radius, 0),  # Top Right
    (0.625 * 0.75 - length / 2 + corner_radius, 0)   # Top Left
]
# --- Create the base rectangular plate ---
plate = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Add the holes ---
for center_x, center_y in hole_centers:
    plate = plate.faces(">Z").workplane().hole(2 * hole_radius)
# --- Apply translation ---
plate = plate.translate((0, 0, 0.0225))
# --- Export to STL ---
cq.
# --- Export to
# 定义结果变量
result = plate
# 导出为STL文件
cq.exporters.export(result, "output_282.stl