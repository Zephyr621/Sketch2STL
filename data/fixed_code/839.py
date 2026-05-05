import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.2577 * 0.75)
    .lineTo(0.5357 * 0.75, 0.2577 * 0.75)
    .lineTo(0.5357 * 0.75, 0.5357 * 0.75)
    .lineTo(0.0, 0.5357 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.5239)
)
# Coordinate System Transformation for Part 1
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.5239, 0))
# --- Part 2 ---
part_2 = (
    cq.Workplane("XY")
    .rect(0.6246 * 0.6246, 0.3697 * 0.6246)
    .extrude(-0.4659)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_839.stl