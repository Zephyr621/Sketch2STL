import cadquery as cq
import math
from cadquery.vis import show
# --- Parameters from JSON ---
outer_radius = 0.375 * 0.75
inner_radius = 0.2812 * 0.75
hole1_center = (0.1875 * 0.75 - outer_radius, 0.0937 * 0.75 - outer_radius)
hole2_center = (0.5625 * 0.75 - outer_radius, 0.0937 * 0.75 - outer_radius)
hole3_center = (0.5625 * 0.75 - outer_radius, 0.2812 * 0.75 - outer_radius)
hole4_center = (0.6562 * 0.75 - outer_radius, 0.0937 * 0.75 - outer_radius)
hole_radius = 0.0313 * 0.75
plate_thickness = 0.0125
# --- Create Plate ---
plate = cq.Workplane("XY").circle(outer_radius).extrude(plate_thickness)
# --- Add Holes ---
plate = plate.faces(">Z").workplane().pushPoints([hole1_center]).hole(2 * hole_radius)
plate = plate.faces(">Z").workplane().pushPoints([hole2_center]).hole(2 * hole_radius)
plate = plate.faces(">Z").workplane().
# Export
# 定义结果变量
result = plate
# 导出为STL文件
cq.exporters.export(result, "output_2797.stl