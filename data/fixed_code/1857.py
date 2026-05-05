import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.1985)
    .lineTo(0.5357, 0.1985)
    .lineTo(0.5357, 0.5523)
    .lineTo(0.2143, 0.5523)
    .lineTo(0.2143, 0.2087)
    .lineTo(0.0, 0.2087)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0418 * 2)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0846, 0))
# --- Assembly ---
assembly = part_1
cq.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1857.stl