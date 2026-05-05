import cadquery as cq
# --- Part 1: L-shaped profile ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.25 * 0.75)
    .lineTo(0.25 * 0.75, 0.25 * 0.75)
    .lineTo(0.25 * 0.75, 0.625 * 0.75)
    .lineTo(0.0, 0.625 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(-0.5)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# Export to STL
cq.
cq.
cq.exporters
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_848.stl