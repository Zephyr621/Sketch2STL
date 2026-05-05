import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.075 * 0.75)
    .lineTo(0.675 * 0.75, 0.075 * 0.75)
    .lineTo(0.675 * 0.75, 0.1425 * 0.75)
    .lineTo(0.375 * 0.75, 0.1425 * 0.75)
    .lineTo(0.375 * 0.75, 0.075 * 0.75)
    .lineTo(0.0, 0.075 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0099)
)
# Add hole
hole_center_x = 0.675 * 0.75
hole_center_y = 0.075 * 0.75
hole_radius = 0.0375 * 0.75
part_1 = part_1.faces(">Z").workplane().pushPoints([(hole_center_x - (0.75 * 0.75)/2,
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2528.stl