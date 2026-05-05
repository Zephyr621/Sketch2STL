import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.25 * 0.25, 0.0)
    .lineTo(0.25 * 0.25, 0.0036 * 0.25)
    .lineTo(0.0036 * 0.25, 0.0036 * 0.25)
    .lineTo(0.0036 * 0.25, 0.0352 * 0.25)
    .lineTo(0.0, 0.0352 * 0.25)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(-0.75)
)
# Add the cutout
cutout_wp = cq.Workplane("XY").moveTo(0.1229 * 0.25, 0.0476 * 0.25).circle(0.0158 * 0.25).extrude(-0.75)
cutout = cutout_wp.cut(cutout_wp.translate((0.2514, 0.0476, 0)))
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# Export
# 定义结果变量
result = cutout_wp
# 导出为STL文件
cq.exporters.export(result, "output_3487.stl