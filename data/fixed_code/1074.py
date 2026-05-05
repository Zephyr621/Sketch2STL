import cadquery as cq
# --- Part 1: L-shaped base ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(0.75 * 0.75, 0)
    .lineTo(0.75 * 0.75, 0.125 * 0.75)
    .lineTo(0.5 * 0.75, 0.125 * 0.75)
    .lineTo(0.5 * 0.75, 0.375 * 0.75)
    .lineTo(0, 0.375 * 0.75)
    .close()
    .extrude(0.5 * 0.75)
)
# --- Part 2: Rectangular extension on top ---
part_2 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(0.25 * 0.375, 0)
    .lineTo(0.25 * 0.375, 0.125 * 0.375)
    .lineTo(0, 0.125 * 0.375)
    .close()
    .extrude(-0.125 * 0.375)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0.5, 0.25, 0))
# --- Assembly ---
assembly = part_1.union(part_2
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1074.stl