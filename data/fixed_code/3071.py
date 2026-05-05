import cadquery as cq
# --- Parameters from JSON ---
length = 0.6 * 0.75  # Scaled length
width = 0.75 * 0.75   # Scaled width
height = 0.075
hole_radius = 0.0375 * 0.75  # Scaled radius
hole1_x = 0.15 * 0.75  # Scaled x-coordinate
hole1_y = 0.15 * 0.75  # Scaled y-coordinate
hole2_x = 0.6 * 0.75  # Scaled x-coordinate
hole2_y = 0.15 * 0.75  # Scaled y-coordinate
# --- Create the base rectangular plate ---
plate = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Add the holes ---
plate = (
    plate.faces(">Z")
    .workplane()
    .pushPoints([(hole1_x - length/2, hole1_y - width/2), (hole2_x - length/2, hole2_y - width/2)])
    .hole(2 * hole_radius)
)
# --- Export to STL
# Export
# 定义结果变量
result = plate
# 导出为STL文件
cq.exporters.export(result, "output_3071.stl