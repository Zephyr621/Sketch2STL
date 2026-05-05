import cadquery as cq
# --- Parameters from JSON ---
length = 0.255 * 0.75  # Scaled length
width = 0.75 * 0.75  # Scaled width
height = 0.12
hole_radius = 0.0562 * 0.75  # Scaled radius
hole1_x = 0.0615 * 0.75  # Scaled x position
hole1_y = 0.1403 * 0.75  # Scaled y position
hole2_x = 0.1863 * 0.75  # Scaled x position
hole2_y = 0.1403 * 0.75  # Scaled y position
# --- Create the base rectangular block ---
block = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Create the holes ---
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
# --- Export to STL ---
cq.cq.exporters.export(block,
# 定义结果变量
result = block
# 导出为STL文件
cq.exporters.export(result, "output_882.stl