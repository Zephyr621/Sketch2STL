import cadquery as cq
# --- Part 1 ---
sketch_scale = 0.75
length = 0.75 * sketch_scale
width = 0.6562 * sketch_scale
height = 0.1525
hole_radius = 0.0375 * sketch_scale
hole1_x = 0.0937 * sketch_scale
hole1_y = 0.1875 * sketch_scale
hole2_x = 0.6402 * sketch_scale
hole2_y = 0.5625 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(length, 0.0)
    .lineTo(length, width)
    .lineTo(0.0, width)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(height)
)
# Add holes
part_1 = (
    part_1.faces(">Z")
    .workplane()
    .pushPoints([(hole1_x - length/2, hole1_y - width/2), (hole2_x - length/2, hole2_y - width/2)])
    .hole(2 * hole_radius)
)
# --- Coordinate System Transformation for Part 1 ---
part_
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1195.stl