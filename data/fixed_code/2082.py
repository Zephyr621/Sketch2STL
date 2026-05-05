import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.1083)
    .lineTo(0.5625, 0.1083)
    .lineTo(0.5625, 0.4286)
    .lineTo(0.1875, 0.4286)
    .lineTo(0.1875, 0.0833)
    .lineTo(0.0937, 0.0833)
    .lineTo(0.0937, 0.2812)
    .lineTo(0.0, 0.2812)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.2984)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.2984, 0))
# --- Assembly ---
assembly = part_1
cq
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2082.stl