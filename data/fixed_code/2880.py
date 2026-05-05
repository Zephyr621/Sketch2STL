import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0061 * 0.75)
    .lineTo(0.1789 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.0788 * 0.75)
    .lineTo(0.5703 * 0.75, 0.0788 * 0.75)
    .lineTo(0.5703 * 0.75, 0.2769 * 0.75)
    .lineTo(0.1876 * 0.75, 0.2769 * 0.75)
    .lineTo(0.1876 * 0.75, 0.0061 * 0.75)
    .close()
    .extrude(0.0156)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0156, 0))
# --- Assembly ---
assembly = part
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2880.stl