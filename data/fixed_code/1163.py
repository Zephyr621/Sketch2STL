import cadquery as cq
# --- Parameters from JSON ---
length = 0.75 * 0.75  # Scaled length
width = 0.4464 * 0.75  # Scaled width
height = 0.04
hole_radius = 0.0204 * 0.75  # Scaled hole radius
hole1_x = 0.0711 * 0.75  # Scaled x position
hole1_y = 0.1489 * 0.75  # Scaled y position
hole2_x = 0.5782 * 0.75  # Scaled x position
hole2_y = 0.1489 * 0.75  # Scaled y position
hole3_x = 0.6765 * 0.75  # Scaled x position
hole3_y = 0.1489 * 0.75  # Scaled y position
hole4_x = 0.6114 * 0.75  # Scaled x position
hole4_y = 0.1489 * 0.75  # Scaled y position
# --- Create the base rectangular plate ---
plate = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Add the holes ---
plate = (
    plate.faces(">Z")
    .workplane()
    .pushPoints([(hole1_x - length/2, hole1_y - width/2), (hole2
# Export
# 定义结果变量
result = plate
# 导出为STL文件
cq.exporters.export(result, "output_1163.stl