import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.1054 * 0.75, 0.0)
    .lineTo(0.1054 * 0.75, 0.0455 * 0.75)
    .lineTo(0.5288 * 0.75, 0.0455 * 0.75)
    .lineTo(0.5288 * 0.75, 0.3827 * 0.75)
    .lineTo(0.6495 * 0.75, 0.3827 * 0.75)
    .lineTo(0.6495 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.4402 * 0.75)
    .lineTo(0.6495 * 0.75, 0.4402 * 0.75)
    .lineTo(0.6495 * 0.75, 0.0818 * 0.75)
    .lineTo(0.0, 0.0818 * 0.75)
    .
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1384.stl