import cadquery as cq
# --- Parameters from JSON ---
length = 0.75 * 0.75  # Scaled length
width = 0.4286 * 0.75  # Scaled width
height = 0.1268
hole_radius = 0.0714 * 0.75  # Scaled radius
square_x = 0.5357 * 0.75  # Scaled square x
square_y = 0.2143 * 0.75  # Scaled square y
square_size = (0.4829 - 0.3214) * 0.75  # Scaled square size
# --- Create the base rectangular block ---
block = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Create the circular hole ---
block = block.faces(">Z").workplane().circle(hole_radius).cutThruAll()
# --- Export to STL ---
cq.
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
cq.exporters.export(result, "output_2786.stl