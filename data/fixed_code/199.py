import cadquery as cq
# --- Parameters from JSON ---
length = 0.75 * 0.75  # Scaled length
width = 0.5833 * 0.75  # Scaled width
height = 0.1705
hole_center_x = 0.375 * 0.75  # Scaled center x
hole_center_y = 0.2945 * 0.75  # Scaled center y
hole_radius = 0.0865 * 0.75  # Scaled radius
# --- Create the rectangular block ---
block = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Create the hole ---
block = block.faces(">Z").workplane().hole(2 * hole_radius)
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
# --- Export to STL ---
cq.exp
# 定义结果变量
result = block
# 导出为STL文件
cq.exporters.export(result, "output_199.stl