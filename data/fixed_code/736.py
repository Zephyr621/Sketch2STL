import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.15)
    .lineTo(0.6167, 0.15)
    .lineTo(0.6167, 0.2165)
    .lineTo(0.0221, 0.2165)
    .lineTo(0.0221, 0.15)
    .lineTo(0.0, 0.15)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0273)
)
# Create the hole
hole_center_x = 0.0221 * 0.75
hole_center_y = 0.1042 * 0.75
hole_radius = 0.0059 * 0.75
part_1 = (
    part_1.faces(">Z")
    .workplane()
    .circle(hole_radius)
    .cutThruAll()
)
# --- Coordinate System Transformation
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_736.stl