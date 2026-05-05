import cadquery as cq
# --- Parameters from JSON ---
length = 0.75 * 0.75  # Scaled length
width = 0.4687 * 0.75  # Scaled width
height = 0.0188
hole_radius = 0.0082 * 0.75  # Scaled radius
hole1_x = 0.0341 * 0.75  # Scaled x position of hole 1
hole1_y = 0.2099 * 0.75  # Scaled y position of hole 2
hole2_x = 0.7148 * 0.75  # Scaled x position of hole 2
hole2_y = 0.2099 * 0.75  # Scaled y position of hole 3
hole3_x = 0.7148 * 0.75  # Scaled x position of hole 4
hole3_y = 0.2099 * 0.75  # Scaled y position of hole 4
# --- Create the base rectangular plate ---
plate = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Add the holes ---
plate = (
    plate.faces(">Z")
    .workplane()
    .pushPoints([(hole1_x - length/2, hole1_y - width/2), (hole2_x - length/2, hole2_y - width/2)])
    .hole(2 * hole_radius)
# Export
# 定义结果变量
result = plate
# 导出为STL文件
cq.exporters.export(result, "output_3232.stl