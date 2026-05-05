import cadquery as cq
# --- Parameters from JSON ---
length = 0.75
width = 0.2462
height = 0.0035
sketch_scale = 0.75
hole_radius = 0.0238 * sketch_scale
corner_radius = 0.0625 * sketch_scale
# Hole centers (scaled)
hole_centers = [
    (0.125 * sketch_scale - length/2, 0.125 * sketch_scale - width/2),
    (0.375 * sketch_scale - length/2, 0.125 * sketch_scale - width/2),
    (0.625 * sketch_scale - length/2, 0.125 * sketch_scale - width/2),
    (0.625 * sketch_scale - length/2, 0.25 * sketch_scale - width/2)
]
# --- Create the base rectangular plate ---
plate = cq.Workplane("XY").rect(length * sketch_scale, width * sketch_scale).extrude(height)
# --- Cut the holes ---
for center_x, center_y in hole_centers:
    plate = plate.faces(">Z").workplane().pushPoints([(center_x, center_y)]).hole(2 * hole_
# Export
# 定义结果变量
result = plate
# 导出为STL文件
cq.exporters.export(result, "output_948.stl