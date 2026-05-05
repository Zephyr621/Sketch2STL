import cadquery as cq
# --- Parameters from JSON ---
length = 0.75 * 0.75
width = 0.375 * 0.75
height = 0.125
sketch_scale = 0.75
# Scaled dimensions
scaled_length = length * sketch_scale
scaled_width = width * sketch_scale
scaled_height = height
# Hole parameters (scaled)
hole_center1 = (0.125 * sketch_scale - scaled_length / 2, 0.1875 * sketch_scale - scaled_width / 2)
hole_center2 = (0.625 * sketch_scale - scaled_length / 2, 0.1875 * sketch_scale - scaled_width / 2)
hole_radius = 0.0625 * sketch_scale
# --- Create the base rectangular box ---
box = cq.Workplane("XY").rect(scaled_length, scaled_width).extrude(scaled_height)
# --- Add the holes ---
box = box.faces(">Z").workplane().pushPoints([hole_center1]).hole(2 * hole_radius)
box = box.faces(">Z").workplane().pushPoints([hole_center2]).hole(2 * hole_radius)
# --- Apply rotation and translation
# Export
# 定义结果变量
result = box
# 导出为STL文件
cq.exporters.export(result, "output_1663.stl