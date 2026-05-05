import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.7143 * 0.7414, 0.0)
    .lineTo(0.7143 * 0.7414, 0.4803 * 0.7414)
    .lineTo(0.0, 0.4803 * 0.7414)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0059)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0059, 0))
# --- Part 2 ---
part_2 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.0105 * 0.4936, 0.0)
    .lineTo(0.0105 * 0.4936, 0.4936 * 0.4936)
    .lineTo(0.0, 0.4936 * 0.4936)
    .lineTo(0.0, 0.0)
    .close()
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1598.stl