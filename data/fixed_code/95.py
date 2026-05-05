import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.2596 * 0.75)
    .lineTo(0.0013 * 0.75, 0.0)
    .lineTo(0.7423 * 0.75, 0.0)
    .lineTo(0.7423 * 0.75, 0.2409 * 0.75)
    .lineTo(0.75 * 0.75, 0.2409 * 0.75)
    .lineTo(0.75 * 0.75, 0.5181 * 0.75)
    .lineTo(0.7332 * 0.75, 0.5181 * 0.75)
    .lineTo(0.7332 * 0.75, 0.2596 * 0.75)
    .lineTo(0.0, 0.2596 * 0.75)
    .close()
    .extrude(0.0222)
)
# --- Assembly ---
assembly = part_1
cq.
# Export to STL
cq.exporters
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_95.stl