import cadquery as cq
# --- Parameters from JSON ---
length = 0.75
width = 0.5357
height = 0.0161
sketch_scale = 0.75
hole1_center = (0.0951 * sketch_scale, 0.3214 * sketch_scale)
hole2_center = (0.6543 * sketch_scale, 0.1607 * sketch_scale)
hole3_center = (0.6929 * sketch_scale, 0.3214 * sketch_scale)
hole_radius = 0.0496 * sketch_scale
# --- Create the base rectangular plate ---
plate = (
    cq.Workplane("XY")
    .rect(length * sketch_scale, width * sketch_scale)
    .extrude(height)
)
# --- Create the holes ---
plate = (
    plate.faces(">Z")
    .workplane()
    .pushPoints([hole1_center])
    .hole(2 * hole_radius)
)
plate = (
    plate.faces(">Z")
    .workplane()
    .pushPoints([hole2_center])
    .hole(2 * hole_radius)
)
plate = (
    plate.faces(">Z")
    .workplane
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1543.stl