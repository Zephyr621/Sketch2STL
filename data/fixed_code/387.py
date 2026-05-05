import cadquery as cq
# --- Parameters from JSON ---
length = 0.75 * 0.75  # Scaled length
width = 0.2753 * 0.75  # Scaled width
height = 0.0052  # Extrusion depth
hole_radius = 0.0021 * 0.75  # Scaled radius
hole1_x = 0.0311 * 0.75  # Scaled x-coordinate for hole 1
hole2_x = 0.7222 * 0.75  # Scaled x-coordinate for hole 2
hole3_x = 0.6908 * 0.75  # Scaled x-coordinate for hole 3
# --- Create the base rectangular plate ---
plate = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Add the holes ---
hole1 = cq.Workplane("XY").moveTo(hole1_x - length/2, hole1_y - width/2).circle(hole_radius).extrude(height)
hole2 = cq.Workplane("XY").moveTo(hole2_x - length/2, hole2_y - width/2).circle(hole_radius).extrude(height)
hole3 = cq.Workplane("XY").moveTo(hole3_x - length/2, hole3_y - width/2).circle(hole_radius).extrude(height)
# ---
# Export
# 定义结果变量
result = hole3
# 导出为STL文件
cq.exporters.export(result, "output_387.stl