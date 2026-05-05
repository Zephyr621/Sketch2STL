import cadquery as cq
import math
from cadquery.vis import show
# --- Parameters from JSON ---
outer_radius = 0.3257 * 0.75
inner_radius = 0.2143 * 0.75
extrusion_depth = 0.4286
sketch_scale = 0.75
# Scaled values
scaled_outer_radius = outer_radius * sketch_scale
scaled_inner_radius = inner_radius * sketch_scale
# --- Create the Cylinder ---
cylinder = (
    cq.Workplane("XY")
    .circle(scaled_outer_radius)
    .extrude(extrusion_depth)
)
# --- Create the Hexagon ---
hexagon = (
    cq.Workplane("XY")
    .moveTo(0.1071 * sketch_scale, 0.6429 * sketch_scale)
    .lineTo(0.6429 * sketch_scale, 0.3257 * sketch_scale)
    .lineTo(0.6429 * sketch_scale, 0.6429 * sketch_scale)
    .close()
    .extrude(extrusion_depth)
)
# --- Cut the Inner Circle ---
inner_circle = (
    cq.Workplane("XY")
    .circle(scaled_inner_radius)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_935.stl