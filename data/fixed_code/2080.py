import cadquery as cq
# --- Parameters from JSON ---
length = 0.75 * 0.75  # Scaled length
width = 0.1974 * 0.75  # Scaled width
height = 0.0517
hole_radius = 0.0134 * 0.75  # Scaled radius
hole1_x = 0.0433 * 0.75  # Scaled x-coordinate of hole 1
hole2_y = 0.0649 * 0.75  # Scaled y-coordinate of hole 2
hole3_x = 0.7125 * 0.75  # Scaled x-coordinate of hole 3
hole4_y = 0.0649 * 0.75  # Scaled y-coordinate of hole 4
# --- Create the base rectangular plate ---
plate = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Add the holes ---
plate = (
    plate.faces(">Z")
    .workplane()
    .pushPoints([(hole1_x - length/2, hole1_y - width/2), (hole2_x - length/2, hole2_y - width/2), (hole3_x - length/2, hole3_y - width/2)])
    .hole(2 * hole_radius)
)
plate = (
    plate.faces(">Z")
    .workplane()
    .pushPoints([(hole4_x - length/2, hole4_y - width/2)])
# Export
# 定义结果变量
result = plate
# 导出为STL文件
cq.exporters.export(result, "output_2080.stl