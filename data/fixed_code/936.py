import cadquery as cq
# --- Parameters from JSON ---
length = 0.75 * 0.75  # Scaled by sketch_scale
width = 0.4 * 0.75  # Scaled by sketch_scale
height = 0.0167
hole_radius = 0.0058 * 0.75  # Scaled by sketch_scale
hole1_x = 0.375 * 0.75  # Scaled by sketch_scale
hole1_y = 0.2083 * 0.75  # Scaled by sketch_scale
hole2_x = 0.625 * 0.75  # Scaled by sketch_scale
hole2_y = 0.1957 * 0.75  # Scaled by sketch_scale
hole3_x = 0.375 * 0.75  # Scaled by sketch_scale
hole3_y = 0.5262 * 0.75  # Scaled by sketch_scale
hole4_x = 0.6852 * 0.75  # Scaled by sketch_scale
hole4_y = 0.1957 * 0.75  # Scaled by sketch_scale
# --- Create the base rectangular plate ---
plate = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Add the holes ---
plate = (
    plate.faces(">Z")
    .workplane()
    .pushPoints([(hole1_x - length/2, hole1_y - width/2), (hole2_x - length/2, hole2_y - width/2), (hole3_x - length/2, hole3_y - width/2)])
# Export
# 定义结果变量
result = plate
# 导出为STL文件
cq.exporters.export(result, "output_936.stl