import cadquery as cq
# --- Part 1 ---
sketch_scale = 0.75
length = 0.75 * sketch_scale
width = 0.1846 * sketch_scale
height = 0.1943 * sketch_scale
hole_center_x = 0.375 * sketch_scale
hole_center_y = 0.0923 * sketch_scale
hole_radius = 0.0517 * sketch_scale
extrude_depth = 0.2098 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(length, 0)
    .lineTo(length, width)
    .lineTo(0, width)
    .close()
    .extrude(extrude_depth)
    .faces(">Z").workplane().moveTo(hole_center_x - length/2, hole_center_y - width/2).circle(hole_radius).cutThruAll()
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.1943 * sketch_scale, 0
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1420.stl