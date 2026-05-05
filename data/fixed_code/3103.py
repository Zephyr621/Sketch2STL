import cadquery as cq
from math import *
# --- Parameters from JSON ---
length = 0.75
width = 0.6387
height = 0.0082
sketch_scale = 0.75
hole1_center = (0.0437 * sketch_scale, 0.2056 * sketch_scale)
hole2_center = (0.7174 * sketch_scale, 0.2056 * sketch_scale)
hole3_center = (0.6401 * sketch_scale, 0.2056 * sketch_scale)
hole4_center = (0.7174 * sketch_scale, 0.4719 * sketch_scale)
hole5_center = (0.6893 * sketch_scale, 0.2056 * sketch_scale)
hole6_radius = 0.0273 * sketch_scale
# --- Create the base rectangular plate ---
plate = cq.Workplane("XY").rect(length * sketch_scale, width * sketch_scale).extrude(height)
# --- Create the holes ---
plate = (
    plate.faces(">Z")
    .workplane()
    .pushPoints([hole1_center, hole2_center, hole3_center, hole4_center])
    .hole(hole1_radius * 2)
)
plate = (
    plate.faces(">Z")
    .workplane()
    .pushPoints([hole2_center])
# Export
# 定义结果变量
result = plate
# 导出为STL文件
cq.exporters.export(result, "output_3103.stl