import cadquery as cq
# --- Parameters from JSON ---
length = 0.75 * 0.75  # Scaled length
width = 0.1339 * 0.75  # Scaled width
height = 0.067
hole_radius = 0.0441 * 0.75  # Scaled radius
hole1_x = 0.0857 * 0.75  # Scaled x position
hole2_x = 0.6697 * 0.75  # Scaled y position
hole3_x = 0.6179 * 0.75  # Scaled x position
hole4_x = 0.6179 * 0.75  # Scaled y position
# --- Create the base rectangular bar ---
bar = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
)
# --- Create the holes ---
bar = (
    bar.faces(">Z")
    .workplane()
    .pushPoints([(hole1_x - length/2, hole2_x - width/2), (hole3_x - length/2, hole3_x - width/2)])
    .hole(2 * hole_radius)
)
bar = (
    bar.faces(">Z")
    .workplane()
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3315.stl