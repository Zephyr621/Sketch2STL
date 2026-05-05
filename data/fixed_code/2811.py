import cadquery as cq
# --- Parameters from JSON ---
length = 0.75
width = 0.5
height = 0.375
sketch_scale = 0.75
hole_radius = 0.05  # Adjust for desired radius
# Scaled values
scaled_length = length * sketch_scale
scaled_width = width * sketch_scale
scaled_hole_radius = hole_radius * sketch_scale
# Hole centers (scaled)
hole1_x = 0.125 * sketch_scale
hole1_y = 0.125 * sketch_scale
hole2_x = 0.625 * sketch_scale
hole2_y = 0.125 * sketch_scale
# --- Create the base rectangular box ---
box = cq.Workplane("XY").rect(scaled_length, scaled_width).extrude(height)
# --- Cut out the holes ---
box = box.faces(">Z").workplane().pushPoints([(hole1_x - scaled_length/2, hole1_y - scaled_width/2)]).hole(2 * scaled_hole_radius)
box = box.faces(">Z").workplane().pushPoints([(hole2_x - scaled_length/2, hole2_y - scaled_width/2)]).hole(2 * scaled_hole_radius)
# --- Apply rotation and translation ---
box = box.rotate((0, 0
# Export
# 定义结果变量
result = box
# 导出为STL文件
cq.exporters.export(result, "output_2811.stl