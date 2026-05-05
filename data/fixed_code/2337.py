import cadquery as cq
# --- Parameters from JSON ---
length = 0.75 * 0.75  # Scaled length
width = 0.2753 * 0.75  # Scaled width
height = 0.0816
hole_center_x = 0.375 * 0.75  # Scaled center x
hole_center_y = 0.1324 * 0.75  # Scaled center y
hole_radius = 0.0242 * 0.75  # Scaled radius
# --- Create the base rectangular block ---
block = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Create the hole ---
block = block.faces(">Z").workplane().moveTo(hole_center_x - length/2, hole_center_y - width/2).circle(hole_radius).cutThruAll()
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# 定义结果变量
result = block
# 导出为STL文件
cq.exporters.export(result, "output_2337.stl