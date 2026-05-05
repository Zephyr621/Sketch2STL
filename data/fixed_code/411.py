import cadquery as cq
# --- Part 1: Rectangular Plate with Circular Hole ---
sketch_scale = 0.75
length = 0.75 * sketch_scale
width = 0.45 * sketch_scale
height = 0.025
hole_center_x = 0.25 * sketch_scale
hole_center_y = 0.15 * sketch_scale
hole_radius = 0.075 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(length, 0)
    .lineTo(length, width)
    .lineTo(0.6 * sketch_scale, width)
    .lineTo(0.6 * sketch_scale, 0.45 * sketch_scale)
    .lineTo(0, 0.45 * sketch_scale)
    .lineTo(0, 0)
    .close()
    .extrude(height)
)
# Create the hole
part_1 = part_1.faces(">Z").workplane().center(hole_center_x - length/2, hole_center_y - width/2).circle(hole_radius).cutThruAll()
# --- Coordinate System Transformation for Part 1 ---
part_1 =
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_411.stl