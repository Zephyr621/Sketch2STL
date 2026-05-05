import cadquery as cq
# --- Parameters from JSON ---
length = 0.75 * 0.75  # Scaled length
width = 0.75 * 0.75   # Scaled width
height = 0.0107
hole_radius = 0.0058 * 0.75  # Scaled radius
hole1_x = 0.0857 * 0.75  # Scaled x-coordinate
hole1_y = 0.2804 * 0.75  # Scaled y-coordinate
hole2_x = 0.6671 * 0.75  # Scaled x-coordinate
hole2_y = 0.2804 * 0.75  # Scaled y-coordinate
# --- Create the base square plate ---
plate = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Add the holes ---
hole1 = (
    cq.Workplane("XY")
    .moveTo(hole1_x - length/2, hole1_y - width/2)
    .circle(hole_radius)
    .extrude(height + 0.001)  # Extrude slightly more to ensure complete cut
)
hole2 = (
    cq.Workplane("XY")
    .moveTo(hole2_x - length/2, hole2_y - width/2)
    .circle(hole_radius)
    .extrude(height + 0.001)  # Extrude slightly more to ensure complete cut
)
# Export
# 定义结果变量
result = plate
# 导出为STL文件
cq.exporters.export(result, "output_380.stl