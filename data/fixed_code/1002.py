import cadquery as cq
from math import radians
# --- Parameters from JSON ---
length = 0.75 * 0.75  # Scaled length
width = 0.25 * 0.75  # Scaled width
height = 0.0375
hole_radius = 0.0312 * 0.75  # Scaled radius
hole1_x = 0.0937 * 0.75  # Scaled x position
hole1_y = 0.125 * 0.75  # Scaled y position
hole2_x = 0.6563 * 0.75  # Scaled x position
hole2_y = 0.125 * 0.75  # Scaled y position
# --- Create the base rectangular bracket ---
bracket = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Create the holes ---
bracket = (
    bracket.faces(">Z")
    .workplane()
    .pushPoints([((hole1_x - length/2), (hole1_y - width/2))])
    .circle(hole_radius)
    .cutThruAll()
)
bracket = (
    bracket.faces(">Z")
    .workplane()
    .pushPoints([(hole2_x - length/2), (hole2_y - width/2)])
    .circle(hole_radius
# Export
# 定义结果变量
result = bracket
# 导出为STL文件
cq.exporters.export(result, "output_1002.stl