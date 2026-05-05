import cadquery as cq
from math import *
# --- Parameters from JSON ---
length = 0.75
width = 0.3125
height = 0.0938
sketch_scale = 0.75
hole_radius = 0.0469 * sketch_scale
hole1_center = (0.0872 * sketch_scale, 0.1406 * sketch_scale)
hole2_center = (0.6281 * sketch_scale, 0.1406 * sketch_scale)
# --- Create the base rectangular block ---
block = cq.Workplane("XY").rect(length * sketch_scale, width * sketch_scale).extrude(height)
# --- Add the holes ---
block = (
    block.faces(">Z")
    .workplane()
    .pushPoints([
        (hole1_center[0] - (length * sketch_scale)/2, hole1_center[1] - (width * sketch_scale)/2),
        (hole2_center[0] - (length * sketch_scale)/2, hole2_center[1] - (width * sketch_scale)/2)
    ])
    .hole(hole_radius * 2)
)
# --- Export to STL ---
cq.
# ---
# 定义结果变量
result = block
# 导出为STL文件
cq.exporters.export(result, "output_2981.stl