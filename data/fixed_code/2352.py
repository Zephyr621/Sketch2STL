import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.2344 * 0.75)
    .lineTo(0.2344 * 0.75, 0.2344 * 0.75)
    .lineTo(0.2344 * 0.75, 0.4687 * 0.75)
    .lineTo(0.0, 0.4687 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.375)
)
# --- Assembly ---
assembly = part_1
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2352.stl