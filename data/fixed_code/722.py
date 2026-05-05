import cadquery as cq
# --- Parameters from JSON ---
length = 0.75 * 0.75  # Scaled by sketch_scale
width = 0.2083 * 0.75  # Scaled by sketch_scale
height = 0.0292
hole_radius = 0.0158 * 0.75  # Scaled by sketch_scale
hole_centers = [
    (0.1667 * 0.75 - length / 2, 0.0833 * 0.75 - width / 2),
    (0.1667 * 0.75 - length / 2, 0.2083 * 0.75 - width / 2),
    (0.4167 * 0.75 - length / 2, 0.0833 * 0.75 - width / 2),
    (0.4167 * 0.75 - length / 2, 0.2083 * 0.75 - width / 2)
]
# --- Create the base rectangular plate ---
plate = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Cut the central hole ---
plate = plate.faces(">Z").workplane().pushPoints([(-length / 2 + hole_centers[0], -width / 2 + hole_centers[1]]).hole(2 * hole_radius)
# --- Cut the smaller holes ---
for center_x, center_y in hole_centers:
    plate = plate.faces(">Z").workplane().pushPoints([(center_x, center_y)]).hole(2 * hole_radius)
# --- Export to STL ---
# Export
# 定义结果变量
result = plate
# 导出为STL文件
cq.exporters.export(result, "output_722.stl