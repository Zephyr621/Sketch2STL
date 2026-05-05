import cadquery as cq
# --- Part 1: L-shaped base ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(0.5 * 0.5, 0)
    .lineTo(0.5 * 0.5, 0.125 * 0.5)
    .lineTo(0.375 * 0.5, 0.125 * 0.5)
    .lineTo(0.375 * 0.5, 0.25 * 0.5)
    .lineTo(0.125 * 0.5, 0.25 * 0.5)
    .lineTo(0.125 * 0.5, 0.625 * 0.5)
    .lineTo(0, 0.625 * 0.5)
    .close()
    .extrude(0.375 * 0.5)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.375, 0))
# --- Part 2: Rectangular protrusion ---
part_2 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(0.75 * 0.75, 0)
    .lineTo(0.75 * 0.75,
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_788.stl