import cadquery as cq
# --- Part 1: L-shaped CAD Model ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.0965 * 0.1969, 0.0)
    .lineTo(0.0965 * 0.1969, 0.1969 * 0.1969)
    .lineTo(0.0132 * 0.1969, 0.1969 * 0.1969)
    .lineTo(0.0132 * 0.1969, 0.0239 * 0.1969)
    .lineTo(0.0, 0.0239 * 0.1969)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.75)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (1, 0, 0), -90)
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
# --- Assembly ---
assembly = part_1
cq.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_300.stl