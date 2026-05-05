import cadquery as cq
# --- Parameters from JSON ---
length = 0.75 * 0.75  # Scaled length
width = 0.4167 * 0.75  # Scaled width
height = 0.0417
hole_radius = 0.0208 * 0.75  # Scaled radius
hole1_x = 0.2083 * 0.75  # Scaled x position
hole2_y = 0.2917 * 0.75  # Scaled y position
hole3_x = 0.5167 * 0.75  # Scaled x position
hole4_y = 0.2917 * 0.75  # Scaled y position
# --- Create the base rectangular prism ---
base = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
)
# --- Add the holes ---
hole1 = cq.Workplane("XY").moveTo(hole1_x - length/2, hole1_y - width/2).circle(hole_radius).extrude(height)
hole2 = cq.Workplane("XY").moveTo(hole2_x - length/2, hole2_y - width/2).circle(hole_radius).extrude(height)
hole3 = cq.Workplane("XY").moveTo(hole3_x - length/2, hole3_y - width/2).circle(
# Export
# 定义结果变量
result = hole3
# 导出为STL文件
cq.exporters.export(result, "output_611.stl