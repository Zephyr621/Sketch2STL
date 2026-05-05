import cadquery as cq
# --- Parameters from JSON ---
length = 0.75 * 0.75  # Scaled length
width = 0.4412 * 0.75  # Scaled width
height = 0.2647
hole_radius = 0.0882 * 0.75  # Scaled radius
hole1_x = 0.375 * 0.75  # Scaled x-coordinate
hole1_y = 0.1324 * 0.75  # Scaled y-coordinate
hole2_x = 0.6607 * 0.75  # Scaled x-coordinate
hole2_y = 0.1324 * 0.75  # Scaled y-coordinate
# --- Create the base rectangular block ---
block = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Add the holes ---
block = (
    block.faces(">Z")
    .workplane()
    .pushPoints([(hole1_x - length/2, hole1_y - width/2), (hole2_x - length/2, hole2_y - width/2)])
    .hole(2 * hole_radius)
)
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# ---
# 定义结果变量
result = block
# 导出为STL文件
cq.exporters.export(result, "output_1056.stl