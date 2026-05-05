import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.4203 * 0.75)
    .lineTo(0.3743 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.3274 * 0.75)
    .lineTo(0.4914 * 0.75, 0.6207 * 0.75)
    .lineTo(0.4203 * 0.75, 0.6429 * 0.75)
    .lineTo(0.0, 0.4203 * 0.75)
    .close()
    .extrude(0.3421)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.3421, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.
cq.cq.exporters.export(assembly,
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1671.stl