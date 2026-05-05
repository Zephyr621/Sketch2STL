import cadquery as cq
# --- Part 1: L-shaped CAD Model ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.2743 * 0.75)
    .lineTo(0.5579 * 0.75, 0.2743 * 0.75)
    .lineTo(0.5579 * 0.75, 0.3943 * 0.75)
    .lineTo(0.6964 * 0.75, 0.3943 * 0.75)
    .lineTo(0.6964 * 0.75, 0.2252 * 0.75)
    .lineTo(0.0, 0.2252 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.2197)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.2197, 0))
# --- Assembly ---
assembly = part_1
cq.
# --- Export to
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3065.stl