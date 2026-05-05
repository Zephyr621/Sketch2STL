import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.0304 * 0.75, 0.0)
    .lineTo(0.0304 * 0.75, 0.1768 * 0.75)
    .lineTo(0.7043 * 0.75, 0.1768 * 0.75)
    .lineTo(0.7043 * 0.75, 0.2163 * 0.75)
    .lineTo(0.75 * 0.75, 0.2163 * 0.75)
    .lineTo(0.75 * 0.75, 0.3942 * 0.75)
    .lineTo(0.7043 * 0.75, 0.3942 * 0.75)
    .lineTo(0.7043 * 0.75, 0.2216 * 0.75)
    .lineTo(0.7043 * 0.75, 0.2216 * 0.75)
    .lineTo(0.7043 * 0.75, 0.2359 * 0.75)
    .lineTo(0.7043 * 0.75, 0.2359
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2881.stl