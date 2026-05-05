import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.375, 0.0)
    .lineTo(0.375, 0.0937)
    .lineTo(0.4688, 0.0937)
    .lineTo(0.4688, 0.1875)
    .lineTo(0.7188, 0.1875)
    .lineTo(0.7188, 0.375)
    .lineTo(0.5625, 0.375)
    .lineTo(0.5625, 0.1875)
    .lineTo(0.1875, 0.1875)
    .lineTo(0.1875, 0.375)
    .lineTo(0.0, 0.375)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.1875)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.375, 0))
# --- Assembly ---
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3233.stl