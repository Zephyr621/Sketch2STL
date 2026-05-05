import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.3061)
    .lineTo(0.5053, 0.3061)
    .lineTo(0.5053, 0.6071)
    .lineTo(0.2426, 0.6071)
    .lineTo(0.2426, 0.3061)
    .lineTo(0.0, 0.3061)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0147)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0147, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_492.stl