import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
length = 0.75 * sketch_scale
width = 0.2557 * sketch_scale
height = 0.1328
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0865 * sketch_scale)
    .threePointArc((0.0865 * sketch_scale, 0.0), (0.2507 * sketch_scale, 0.0865 * sketch_scale))
    .lineTo(0.2507 * sketch_scale, 0.1289 * sketch_scale)
    .threePointArc((0.0865 * sketch_scale, 0.2407 * sketch_scale), (0.0, 0.1289 * sketch_scale))
    .lineTo(0.0, 0.0865 * sketch_scale)
    .close()
    .extrude(height)
)
# Add hole
hole_center_x = 0.375 * sketch_scale
hole_center_y = 0.125 * sketch_scale
hole_radius = 0.0615 * sketch_scale
part_1 = part_1.faces(">Z").workplane().pushPoints([(hole_center_x - length/2, hole_center_y - width/2)]).hole(2 *
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_539.stl