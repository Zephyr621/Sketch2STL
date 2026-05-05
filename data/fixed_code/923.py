import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.4687 * 0.4687, 0.0)
    .lineTo(0.4687 * 0.4687, 0.1607 * 0.4687)
    .lineTo(0.3125 * 0.4687, 0.1607 * 0.4687)
    .lineTo(0.3125 * 0.4687, 0.0471 * 0.4687)
    .lineTo(0.1406 * 0.4687, 0.0471 * 0.4687)
    .lineTo(0.1406 * 0.4687, 0.0536 * 0.4687)
    .lineTo(0.0, 0.0536 * 0.4687)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.1875 + 0.1875)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (1, 0, 0), -90)
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
# --- Assembly ---
assembly = part_1
cq.exporters.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_923.stl