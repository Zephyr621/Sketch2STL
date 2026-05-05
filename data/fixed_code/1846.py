import cadquery as cq
# --- Parameters from JSON ---
plate_size = 0.75 * 0.75  # Scaled plate size
hole_radius = 0.0214 * 0.75  # Scaled hole radius
plate_thickness = 0.0429
hole_centers = [
    (0.1607 * 0.75 - plate_size/2, 0.375 * 0.75 - plate_size/2),
    (0.1607 * 0.75 - plate_size/2, 0.5893 * 0.75 - plate_size/2),
    (0.5893 * 0.75 - plate_size/2, 0.375 * 0.75 - plate_size/2)
]
# --- Create the base plate ---
plate = cq.Workplane("XY").rect(plate_size, plate_size).extrude(plate_thickness)
# --- Add the holes ---
for center_x, center_y in hole_centers:
    plate = plate.faces(">Z").workplane().pushPoints([(center_x, center_y)]).hole(2 * hole_radius)
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export
# 定义结果变量
result = plate
# 导出为STL文件
cq.exporters.export(result, "output_1846.stl