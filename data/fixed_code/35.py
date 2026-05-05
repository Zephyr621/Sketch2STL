import cadquery as cq
# --- Parameters from JSON ---
length = 0.75 * 0.75  # Scaled length
width = 0.4375 * 0.75  # Scaled width
height = 0.3125
hole_radius = 0.0312 * 0.75  # Scaled radius
hole1_x = 0.2188 * 0.75  # Scaled x-coordinate of hole 1
hole1_y = 0.1062 * 0.75  # Scaled y-coordinate of hole 1
hole2_x = 0.575 * 0.75  # Scaled x-coordinate of hole 2
hole2_y = 0.2187 * 0.75  # Scaled y-coordinate of hole 2
hole3_x = 0.25 * 0.75  # Scaled x-coordinate of hole 3
hole3_y = 0.2187 * 0.75  # Scaled y-coordinate of hole 3
hole4_x = 0.625 * 0.75  # Scaled x-coordinate of hole 4
hole4_y = 0.2187 * 0.75  # Scaled y-coordinate of hole 4
# --- Create the base rectangular prism ---
base = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Create the holes ---
base = (
    base.faces(">Z")
    .workplane()
# Export
# 定义结果变量
result = base
# 导出为STL文件
cq.exporters.export(result, "output_35.stl