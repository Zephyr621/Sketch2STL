import cadquery as cq
# --- Parameters from JSON ---
length = 0.75 * 0.75  # Scaled length
width = 0.2577 * 0.75  # Scaled width
height = 0.0107
hole_radius = 0.0052 * 0.75  # Scaled radius
hole1_x = 0.0402 * 0.75  # Scaled x position
hole2_x = 0.7386 * 0.75  # Scaled x position
hole3_x = 0.6665 * 0.75  # Scaled y position
hole4_x = 0.6984 * 0.75  # Scaled x position
hole5_y = 0.0854 * 0.75  # Scaled y position
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
    plate.faces(">Z
# Export
# 定义结果变量
result = plate
# 导出为STL文件
cq.exporters.export(result, "output_1003.stl