import cadquery as cq
# --- Parameters from JSON ---
length = 0.4452 * 0.75  # Scaled length
width = 0.75 * 0.75  # Scaled width
height = 0.0148
hole_radius = 0.0395 * 0.75  # Scaled radius
hole1_x = 0.1687 * 0.75  # Scaled x-coordinate of the first hole
hole2_x = 0.4363 * 0.75  # Scaled y-coordinate of the second hole
hole3_x = 0.1563 * 0.75  # Scaled x-coordinate of the third hole
hole_y = 0.0441 * 0.75  # Scaled y-coordinate of the fourth hole
# --- Create the base rectangular plate ---
plate = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Create the central hole ---
plate = plate.faces(">Z").workplane().center(hole1_x - length/2, hole_y - width/2).circle(hole_radius).cutThruAll()
# --- Create the second hole ---
plate = plate.faces(">Z").workplane().center(hole2_x - length/2, hole_y - width/2).circle(hole_radius).cutThruAll()
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# 定义结果变量
result = plate
# 导出为STL文件
cq.exporters.export(result, "output_3371.stl