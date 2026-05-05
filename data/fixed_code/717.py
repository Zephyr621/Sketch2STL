import cadquery as cq
# --- Parameters from JSON ---
length = 0.75 * 0.75  # Scaled length
width = 0.375 * 0.75  # Scaled width
height = 0.0188
hole_radius = 0.0094 * 0.75  # Scaled radius
hole1_x = 0.15 * 0.75  # Scaled x position
hole1_y = 0.075 * 0.75  # Scaled y position
hole2_x = 0.6 * 0.75  # Scaled x position
hole2_y = 0.675 * 0.75  # Scaled y position
hole3_x = 0.675 * 0.75  # Scaled x position
hole3_y = 0.075 * 0.75  # Scaled y position
# --- Create the base rectangular plate ---
plate = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Create the first hole ---
plate = plate.faces(">Z").workplane().center(hole1_x - length/2, hole1_y - width/2).circle(hole_radius).cutThruAll()
# --- Cut the second hole ---
plate = plate.faces(">Z").workplane().center(hole2_x - length/2, hole2_y - width/2).circle(hole_radius).cutThruAll
# Export
# 定义结果变量
result = plate
# 导出为STL文件
cq.exporters.export(result, "output_717.stl