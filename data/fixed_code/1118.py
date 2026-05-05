import cadquery as cq
# --- Parameters from JSON ---
length = 0.75 * 0.75  # Scaled length
width = 0.1557 * 0.75  # Scaled width
height = 0.0425
hole_radius = 0.0199 * 0.75  # Scaled radius
hole_centers = [
    (0.0368 * 0.75 - length / 2, 0.015 * 0.75 - width / 2),
    (0.0368 * 0.75 - length / 2, 0.0721 * 0.75 - width / 2),
    (0.7188 * 0.75 - length / 2, 0.015 * 0.75 - width / 2),
    (0.7188 * 0.75 - length / 2, 0.0721 * 0.75 - width / 2)
]
# --- Create the base rectangular plate ---
plate = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Add the holes ---
for center_x, center_y in hole_centers:
    plate = plate.faces(">Z").workplane().hole(2 * hole_radius)
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# ---
# 定义结果变量
result = plate
# 导出为STL文件
cq.exporters.export(result, "output_1118.stl