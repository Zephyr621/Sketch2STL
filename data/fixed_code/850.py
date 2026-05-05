import cadquery as cq
import math
from cadquery.vis import show
# --- Parameters from JSON ---
outer_radius = 0.3 * 0.75
inner_radius = 0.15 * 0.75
hole_radius = 0.0259 * 0.75
height = 0.0504
sketch_scale = 0.75
# Hole positions (scaled)
hole1_x = 0.0752 * sketch_scale
hole1_y = 0.0752 * sketch_scale
hole2_x = 0.675 * sketch_scale
hole2_y = 0.0752 * sketch_scale
hole3_x = 0.675 * sketch_scale
hole3_y = 0.0752 * sketch_scale
hole4_x = 0.675 * sketch_scale
hole4_y = 0.0752 * sketch_scale
# --- Create the base cylinder ---
cylinder = cq.Workplane("XY").circle(outer_radius).extrude(height)
# --- Cut the inner circle ---
cylinder = cylinder.faces(">Z").workplane().circle(inner_radius).cutThruAll()
# --- Cut the holes ---
cylinder = cylinder.faces(">Z").workplane().pushPoints([(hole1_x - outer_radius, hole1_y - outer_radius)]).hole(2 * hole_radius)
cylinder = cylinder.faces(">Z
# Export
# 定义结果变量
result = cylinder
# 导出为STL文件
cq.exporters.export(result, "output_850.stl