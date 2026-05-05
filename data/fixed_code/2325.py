import cadquery as cq
# --- Parameters from JSON ---
length = 0.75 * 0.75  # Scaled length
width = 0.75 * 0.75  # Scaled width
height = 0.1023
hole_center_x = 0.375 * 0.75  # Scaled hole center x
hole_center_y = 0.3214 * 0.75  # Scaled hole center y
hole_radius = 0.0536 * 0.75  # Scaled hole radius
# --- Create the rectangular plate ---
plate = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Create the hole ---
plate = plate.faces(">Z").workplane().circle(hole_radius).cutThruAll()
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
cq.
# --- Export to ST
# 定义结果变量
result = plate
# 导出为STL文件
cq.exporters.export(result, "output_2325.stl