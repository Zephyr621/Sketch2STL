import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.5192)
    .lineTo(0.7188, 0.5192)
    .lineTo(0.7188, 0.5071)
    .lineTo(0.0, 0.5071)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0057)
)
# --- Assembly ---
assembly = part_1
cq.
# Export to STL
cq.
# Export to STL
cq.
cq.
cq.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1230.stl