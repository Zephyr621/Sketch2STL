import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.3784 * 0.6195, 0.0)
    .lineTo(0.3784 * 0.6195, 0.6195 * 0.6195)
    .lineTo(0.0, 0.6195 * 0.6195)
    .close()
    .extrude(0.7061)
)
# Coordinate System Transformation for Part 1
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2 ---
part_2 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.2458 * 0.2458, 0.0)
    .lineTo(0.2458 * 0.2458, 0.1215 * 0.2458)
    .lineTo(0.0, 0.1215 * 0.2458)
    .close()
    .extrude(-0.0273)
)
# Coordinate System Transformation for Part 2
part_2 = part
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1664.stl