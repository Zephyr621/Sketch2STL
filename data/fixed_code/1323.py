import cadquery as cq
from math import radians
# --- Parameters from JSON ---
plate_length = 0.6903 * 0.75
plate_width = 0.75 * 0.75
plate_height = 0.0034
corner_radius = 0.0458 * 0.75
hole_radius = 0.0265 * 0.75
# Scale parameters
plate_length *= 2  # Assuming plate's length is approximately 0.7031, 0.75, and 0.0034
plate_width *= 2  # Assuming plate's width is approximately 0.7031, 0.75, and 0.0034
corner_radius *= 2
hole_radius *= 2
# --- Create the base square plate ---
plate = cq.Workplane("XY").rect(plate_length, plate_width).extrude(plate_height)
# --- Define corner positions (scaled) ---
corner_positions = [
    (-plate_length / 2 + corner_radius, -plate_width / 2),  # Bottom Left
    (-plate_length / 2 + corner_radius, plate_width / 2 - corner_radius),  # Top Left
    (plate_length / 2 - corner_radius, plate_width / 2 - corner_radius),  # Bottom Right
]
# --- Create corner positions (scaled) ---
corner_positions = [(x * 0.75, y * 0.75) for x, y in corner_positions]
# --- Create holes ---
for pos in corner
# Export
# 定义结果变量
result = plate
# 导出为STL文件
cq.exporters.export(result, "output_1323.stl