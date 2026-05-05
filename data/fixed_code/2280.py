import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.5 * 0.75)
    .lineTo(0.0417 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.4687 * 0.75)
    .lineTo(0.375 * 0.75, 0.4687 * 0.75)
    .lineTo(0.375 * 0.75, 0.5625 * 0.75)
    .lineTo(0.1865 * 0.75, 0.5625 * 0.75)
    .lineTo(0.0, 0.4687 * 0.75)
    .close()
    .extrude(0.0833)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0833, 0))
# --- Assembly ---
assembly = part_1
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2280.stl