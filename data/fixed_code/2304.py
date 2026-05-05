import cadquery as cq
import math
from cadquery.vis import show
# --- Parameters from JSON ---
length = 0.75 * 0.75  # Scaled length
width = 0.2027 * 0.75  # Scaled width
height = 0.1622
hole_radius = 0.0296 * 0.75  # Scaled hole radius
hole_centers = [
    (0.0542 * 0.75 - length / 2, 0.0542 * 0.75 - width / 2),
    (0.6957 * 0.75 - length / 2, 0.0542 * 0.75 - width / 2),
    (0.6957 * 0.75 - length / 2, 0.0542 * 0.75 - width / 2)
]
# --- Create the base rectangular block ---
block = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Add the holes ---
for center_x, center_y in hole_centers:
    block = block.faces(">Z").workplane().pushPoints([(center_x, center_y)]).hole(2 * hole_radius)
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.cq.exporters.export(block
# 定义结果变量
result = block
# 导出为STL文件
cq.exporters.export(result, "output_2304.stl