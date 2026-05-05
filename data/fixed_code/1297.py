import cadquery as cq
from cadquery.vis import show
# --- Parameters from JSON ---
cylinder_radius = 0.375 * 0.75  # Scaled radius
hole1_center = (0.2743 * 0.75, 0.375 * 0.75)
hole2_center = (0.375 * 0.75, 0.3261 * 0.75)
hole3_center = (0.5833 * 0.75, 0.375 * 0.75)
hole4_center = (0.7083 * 0.75, 0.375 * 0.75)
hole5_center = (0.6336 * 0.75, 0.3261 * 0.75)
hole6_radius = 0.1364 * 0.75
extrusion_depth = 0.2386
# --- Create Cylinder ---
cylinder = cq.Workplane("XY").circle(cylinder_radius).extrude(extrusion_depth)
# --- Cut Holes ---
cylinder = cylinder.faces(">Z").workplane().pushPoints([hole1_center]).hole(2 * hole1_radius)
cylinder = cylinder.faces("<Z").workplane().pushPoints([hole2_center]).hole(2 * hole2_radius)
cylinder = cylinder.faces(">Z").workplane().pushPoints([hole3_center]).hole(2 * hole3_radius)
cylinder = cylinder.faces(">Z").workplane().pushPoints([hole4_center]).hole(2 * hole4
# Export
# 定义结果变量
result = cylinder
# 导出为STL文件
cq.exporters.export(result, "output_1297.stl