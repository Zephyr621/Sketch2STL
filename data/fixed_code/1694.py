import cadquery as cq
# --- Parameters from JSON ---
plate_radius = 0.375 * 0.75  # Scaled radius
hole1_center = (0.2526 * 0.75 - 0.1312 * 0.75, 0.375 * 0.75 - 0.375 * 0.75)
hole2_center = (0.5672 * 0.75 - 0.375 * 0.75, 0.375 * 0.75 - 0.375 * 0.75)
hole3_center = (0.6111 * 0.75 - 0.375 * 0.75, 0.375 * 0.75 - 0.375 * 0.75)
hole4_center = (0.7181 * 0.75 - 0.375 * 0.75, 0.375 * 0.75 - 0.375 * 0.75)
plate_height = 0.021
# --- Create the Plate ---
plate = cq.Workplane("XY").circle(plate_radius).extrude(plate_height)
# --- Add Holes ---
plate = (
    plate.faces(">Z")
    .workplane()
    .pushPoints([hole1_center, hole2_center, hole3_center])
    .hole(hole_radius * 2)
)
# --- Export to STL ---
cq.exporters.
# 定义结果变量
result = plate
# 导出为STL文件
cq.exporters.export(result, "output_1694.stl