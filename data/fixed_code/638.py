import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.1667)
    .lineTo(0.5812, 0.1667)
    .lineTo(0.5812, 0.3333)
    .lineTo(0.1667, 0.3333)
    .lineTo(0.1667, 0.1667)
    .lineTo(0.0, 0.1667)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(-0.75)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.75))
# --- Assembly ---
assembly = part_1
cq.
cq.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_638.stl