import cadquery as cq
# --- Parameters from JSON ---
outer_radius = 0.375 * 0.75  # Scaled outer radius
inner_radius = 0.0233 * 0.75  # Scaled inner radius
hole1_center = (0.2345 * 0.75 - 0.375 * 0.75, 0.375 * 0.75 - 0.375 * 0.75)
hole2_center = (0.6207 * 0.75 - 0.375 * 0.75, 0.375 * 0.75 - 0.375 * 0.75)
hole3_center = (0.375 * 0.75 - 0.375 * 0.75, 0.375 * 0.75 - 0.375 * 0.75)
hole4_center = (0.375 * 0.75 - 0.375 * 0.75, 0.375 * 0.75 - 0.375 * 0.75)
plate_thickness = 0.0117
# --- Create the base circular plate ---
plate = cq.Workplane("XY").circle(outer_radius).extrude(plate_thickness)
# --- Create the central hole ---
plate = plate.faces(">Z").workplane().pushPoints([hole1_center]).hole(2 * inner_radius)
plate = plate.faces(">Z").workplane().pushPoints([hole2_center]).hole(2 * inner_radius)
plate = plate.faces(">Z").workplane().pushPoints([hole3_center]).hole
# Export
# 定义结果变量
result = plate
# 导出为STL文件
cq.exporters.export(result, "output_1593.stl