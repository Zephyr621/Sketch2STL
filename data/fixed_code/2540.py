import cadquery as cq
# --- Parameters from JSON ---
length = 0.75 * 0.75  # Scaled length
width = 0.75 * 0.75  # Scaled width
height = 0.0062
hole_radius = 0.0188 * 0.75  # Scaled radius
hole_centers = [
    (0.0938 * 0.75 - length / 2, 0.0938 * 0.75 - width / 2),
    (0.375 * 0.75 - length / 2, 0.6562 * 0.75 - width / 2),
    (0.375 * 0.75 - length / 2, 0.5625 * 0.75 - width / 2),
    (0.6562 * 0.75 - length / 2, 0.0938 * 0.75 - width / 2)
]
# --- Create the base square plate ---
plate = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Add the holes ---
for center_x, center_y in hole_centers:
    plate = plate.faces(">Z").workplane().pushPoints([(center_x, center_y)]).hole(2 * hole_radius)
# --- Export to STL ---
cq.
# --- Export
# 定义结果变量
result = plate
# 导出为STL文件
cq.exporters.export(result, "output_2540.stl