import cadquery as cq
from math import radians
# --- Parameters from JSON ---
length = 0.745
width = 0.596
height = 0.0745
sketch_scale = 0.745
hole1_center = (0.1452, 0.2464)
hole2_center = (0.6115, 0.2464)
hole_radius = 0.0457
# Scale parameters
length *= sketch_scale
width *= sketch_scale
hole1_center = (hole1_center[0] * sketch_scale, hole1_center[1] * sketch_scale)
hole2_center = (hole2_center[0] * sketch_scale, hole2_center[1] * sketch_scale)
hole_radius *= sketch_scale
# --- Create the base plate ---
plate = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Add the holes ---
plate = (
    plate.faces(">Z")
    .workplane()
    .pushPoints([hole1_center])
    .hole(2 * hole_radius)
)
plate = (
    plate.faces(">Z")
    .workplane()
    .pushPoints([hole2_center])
    .hole(2 * hole_radius)
)
# --- Apply translation ---
plate = plate.translate((0.0082, 0
# Export
# 定义结果变量
result = plate
# 导出为STL文件
cq.exporters.export(result, "output_1673.stl