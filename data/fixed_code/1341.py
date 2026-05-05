import cadquery as cq
from cadquery.vis import show 
# --- Parameters from JSON ---
outer_radius = 0.375 * 0.75  # Scaled outer radius
inner_hole_radius = 0.0469 * 0.75
hole1_x = 0.1364 * 0.75
hole1_y = 0.1875 * 0.75
hole2_x = 0.6151 * 0.75
hole2_y = 0.1875 * 0.75
hole3_x = 0.6299 * 0.75
hole3_y = 0.1875 * 0.75
hole4_x = 0.6151 * 0.75
hole4_y = 0.1875 * 0.75
plate_thickness = 0.0938
# --- Create the base circular plate ---
plate = cq.Workplane("XY").circle(outer_radius).extrude(plate_thickness)
# --- Cut the inner hole ---
plate = plate.faces(">Z").workplane().center(hole1_x - (0.375 * 0.75)/2, hole1_y - (0.375 * 0.75)/2).circle(inner_hole_radius).cutThruAll()
# --- Cut the holes ---
plate = plate.faces(">Z").workplane().pushPoints([(hole2_x - (0.375 * 0.75)/2, hole2_y - (0.375 * 0.75)/2)]).hole(2 * inner_hole_radius)
plate = plate.faces(">Z").workplane().pushPoints([(hole3_x - (0.375 *
# Export
# 定义结果变量
result = plate
# 导出为STL文件
cq.exporters.export(result, "output_1341.stl