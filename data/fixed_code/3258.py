import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.0721 * 0.75)
    .lineTo(0.0, 0.0721 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.1629)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0.1853, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.
cq.
cq.
cq.
cq.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3258.stl