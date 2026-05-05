import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: L-shaped Bracket ---
sketch_scale = 0.75
extrude_depth = 0.0714 * sketch_scale
# Scaled dimensions for the base profile
base_profile = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(0.5357 * sketch_scale, 0)
    .threePointArc((0.75 * sketch_scale, 0.2923 * sketch_scale), (0.5357 * sketch_scale, 0.5357 * sketch_scale))
    .lineTo(0.375 * sketch_scale, 0.5357 * sketch_scale)
    .threePointArc((0.2871 * sketch_scale, 0.2871 * sketch_scale), (0.2871 * sketch_scale, 0))
    .close()
    .extrude(extrude_depth)
)
# Create the hole
hole_center_x = 0.2871 * sketch_scale
hole_center_y = 0.3214 * sketch_scale
hole_radius = 0.0964 * sketch_scale
part_1 = (
    base_profile
    .faces(">Z")
    .workplane()
    .circle(hole_radius)
    .cutThruAll
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2757.stl