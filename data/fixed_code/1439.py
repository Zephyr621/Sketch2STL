import cadquery as cq
# --- Part 1: L-shaped base ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(0.75 * 0.75, 0)
    .lineTo(0.75 * 0.75, 0.6 * 0.75)
    .lineTo(0.3 * 0.75, 0.6 * 0.75)
    .lineTo(0.3 * 0.75, 0.75 * 0.75)
    .lineTo(0, 0.75 * 0.75)
    .close()
    .extrude(0.3)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.3, 0))
# --- Part 2: Rectangular Block ---
part_2 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(0.15 * 0.15, 0)
    .lineTo(0.15 * 0.15, 0.075 * 0.15)
    .lineTo(0, 0.075 * 0.15)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1439.stl