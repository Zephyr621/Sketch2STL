import cadquery as cq
# --- Parameters from JSON ---
length = 0.75 * 0.75  # Scaled by sketch_scale
width = 0.2647 * 0.75  # Scaled by sketch_scale
height = 0.4412
hole_radius = 0.0882 * 0.75  # Scaled by sketch_scale
hole_center_x1 = 0.375 * 0.75  # Scaled by sketch_scale
hole_center_x2 = 0.5625 * 0.75  # Scaled by sketch_scale
hole_center_y = 0.1324 * 0.75  # Scaled by sketch_scale
# --- Create the base rectangular block ---
block = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Create the hole ---
block = block.faces(">Z").workplane().moveTo(hole_center_x1 - length/2, hole_center_y - width/2).circle(hole_radius).cutThruAll()
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
#
# 定义结果变量
result = block
# 导出为STL文件
cq.exporters.export(result, "output_1235.stl