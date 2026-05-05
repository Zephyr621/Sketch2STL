import cadquery as cq
from math import *
# Define parameters from JSON data, scaled
sketch_scale = 0.75
# Hole parameters (scaled)
hole_radius = 0.0058 * sketch_scale
# Create the base square plate with rounded corners
plate = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.375 * sketch_scale)
    .lineTo(0.0353 * sketch_scale, 0.375 * sketch_scale)
    .threePointArc((0.7353 * sketch_scale, 0.7353 * sketch_scale), (0.75 * sketch_scale, 0.375 * sketch_scale))
    .lineTo(0.75 * sketch_scale, 0.7353 * sketch_scale)
    .threePointArc((0.7353 * sketch_scale, 0.75 * sketch_scale), (0.0353 * sketch_scale, 0.7353 * sketch_scale))
    .lineTo(0.0353 * sketch_scale, 0.0)
    .threePointArc((0.0353 * sketch_scale, 0.0778 * sketch_scale), (0.0, 0.375 * sketch_scale))
    .close()
    .extrude(0.0125)
)
# Add holes to part 1
part_1 = (
    plate.faces(">Z")
    .workplane()
    .hole(2 * hole_radius)
)
# --- Assembly ---
assembly
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2081.stl