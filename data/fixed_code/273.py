import cadquery as cq
# --- Parameters from JSON ---
length = 0.75 * 0.75  # Scaled length
width = 0.2287 * 0.75  # Scaled width
height = 0.03
hole_radius = 0.0167 * 0.75  # Scaled radius
hole1_x = 0.1406 * 0.75  # Scaled x position
hole1_y = 0.1238 * 0.75  # Scaled y position
hole2_x = 0.6071 * 0.75  # Scaled x position
hole2_y = 0.1238 * 0.75  # Scaled y position
hole3_x = 0.6273 * 0.75  # Scaled x position
hole3_y = 0.1187 * 0.75  # Scaled y position
# --- Create the base rectangular plate ---
plate = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Add the holes ---
plate = (
    plate.faces(">Z")
    .workplane()
    .pushPoints([(hole1_x - length/2, hole1_y - width/2), (hole2_x - length/2, hole2_y - width/2)])
    .hole(hole_radius * 2)
    .faces(">Z")
    .workplane()
    .pushPoints([(hole3_
# Export
# 定义结果变量
result = plate
# 导出为STL文件
cq.exporters.export(result, "output_273.stl