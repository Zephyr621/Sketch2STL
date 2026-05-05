import cadquery as cq
# --- Parameters from JSON ---
length = 0.75 * 0.75  # Scaled length
width = 0.3571 * 0.75  # Scaled width
height = 0.0045
hole_radius = 0.0115 * 0.75  # Scaled radius
hole_centers = [
    (0.0758 * 0.75 - length/2, 0.1612 * 0.75 - width/2),
    (0.675 * 0.75 - length/2, 0.1612 * 0.75 - width/2),
    (0.675 * 0.75 - length/2, 0.4269 * 0.75 - width/2)
]
# --- Create the base rectangular plate ---
plate = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Cut the holes ---
for center_x, center_y in hole_centers:
    plate = plate.faces(">Z").workplane().pushPoints([(center_x, center_y)]).hole(2 * hole_radius)
# --- Export to STL ---
cq.
# --- Export to STL ---
# 定义结果变量
result = plate
# 导出为STL文件
cq.exporters.export(result, "output_1925.stl