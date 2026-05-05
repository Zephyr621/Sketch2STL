import cadquery as cq
# --- Part 1: L-shaped CAD Model ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.0625)
    .lineTo(0.6188, 0.0625)
    .lineTo(0.6188, 0.1607)
    .lineTo(0.1563, 0.1607)
    .lineTo(0.1563, 0.0625)
    .lineTo(0.0, 0.0625)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.1878 + 0.1878)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.375, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1325.stl