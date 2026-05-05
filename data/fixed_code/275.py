import cadquery as cq
# --- Parameters from JSON ---
length = 0.75 * 0.75  # Scaled length
width = 0.2893 * 0.75  # Scaled width
height = 0.0798
hole_radius = 0.0354 * 0.75  # Scaled radius
hole1_x = 0.1364 * 0.75  # Scaled x-coordinate of hole 1
hole2_x = 0.6161 * 0.75  # Scaled x-coordinate of hole 2
hole_y1 = 0.1406 * 0.75  # Scaled y-coordinate of hole 1
hole_y2 = 0.2893 * 0.75  # Scaled y-coordinate of hole 2
# --- Create the base rectangular block ---
block = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Create the holes ---
block = (
    block.faces(">Z")
    .workplane()
    .pushPoints([((hole1_x - length/2), (hole2_x - width/2))])
    .hole(2 * hole_radius)
)
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.cq.exporters.export(
# 定义结果变量
result = block
# 导出为STL文件
cq.exporters.export(result, "output_275.stl