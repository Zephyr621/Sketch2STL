import cadquery as cq
# --- Parameters from JSON ---
length = 0.75 * 0.75  # Scaled length
width = 0.5625 * 0.75  # Scaled width
height = 0.0134
hole_radius = 0.0312 * 0.75  # Scaled hole radius
hole_centers = [
    (0.0469 * 0.75 - length/2, 0.0469 * 0.75 - width/2),  # Scaled center 1
    (0.0469 * 0.75 - length/2, 0.5625 * 0.75 - width/2),
    (0.7031 * 0.75 - length/2, 0.0469 * 0.75 - width/2)
]
# --- Create the base rectangular plate ---
plate = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Add the holes ---
for x, y in hole_centers:
    plate = plate.faces(">Z").workplane().pushPoints([(x, y)]).hole(2 * hole_radius)
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
# 定义结果变量
result = plate
# 导出为STL文件
cq.exporters.export(result, "output_1077.stl