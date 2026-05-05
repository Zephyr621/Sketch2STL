import cadquery as cq
# --- Parameters from JSON ---
length = 0.75 * 0.75  # Scaled length
width = 0.0652 * 0.75  # Scaled width
height = 0.0903  # Height
hole_radius = 0.0321 * 0.75  # Scaled hole radius
hole_center_1 = (0.1807 * 0.75 - length/2, 0.0414 * 0.75 - width/2)  # Scaled and centered
hole_center_2 = (0.5681 * 0.75 - length/2, 0.0414 * 0.75 - width/2)  # Scaled and centered
# --- Create the base rectangular prism ---
rect = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Create the holes ---
rect = rect.faces(">Z").workplane().pushPoints([hole_center_1, hole_center_2]).hole(hole_radius*2)
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export
# 定义结果变量
result = rect
# 导出为STL文件
cq.exporters.export(result, "output_1286.stl