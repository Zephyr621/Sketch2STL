import cadquery as cq
# --- Parameters from JSON ---
length = 0.75
width = 0.4687
height = 0.0125
sketch_scale = 0.75
hole1_center = (0.0208 * sketch_scale, 0.2325 * sketch_scale)
hole1_radius = 0.0058 * sketch_scale
hole2_center = (0.7125 * sketch_scale, 0.0208 * sketch_scale)
hole2_radius = 0.0058 * sketch_scale
hole3_center = (0.7428 * sketch_scale, 0.2325 * sketch_scale)
hole3_radius = 0.0058 * sketch_scale
hole4_center = (0.7125 * sketch_scale, 0.2325 * sketch_scale)
hole4_radius = 0.0058 * sketch_scale
# --- Create the base plate ---
plate = cq.Workplane("XY").rect(length * sketch_scale, width * sketch_scale).extrude(height)
# --- Create the holes ---
plate = (
    plate.faces(">Z")
    .workplane()
    .pushPoints([hole1_center])
    .hole(2 * hole1_radius)
)
plate = (
    plate.faces(">Z")
    .workplane()
# Export
# 定义结果变量
result = plate
# 导出为STL文件
cq.exporters.export(result, "output_3330.stl