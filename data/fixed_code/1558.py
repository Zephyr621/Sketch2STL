import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.3173 * 0.75)
    .lineTo(0.1744 * 0.75, 0.3173 * 0.75)
    .lineTo(0.1744 * 0.75, 0.0)
    .lineTo(0.6198 * 0.75, 0.0)
    .lineTo(0.6198 * 0.75, 0.3865 * 0.75)
    .lineTo(0.6958 * 0.75, 0.3865 * 0.75)
    .lineTo(0.6958 * 0.75, 0.3173 * 0.75)
    .lineTo(0.75 * 0.75, 0.3173 * 0.75)
    .lineTo(0.75 * 0.75, 0.4278 * 0.75)
    .lineTo(0.6958 * 0.75, 0.4278 * 0.75)
    .lineTo(0.6958 * 0.75, 0.3722 * 0.75)
    .lineTo(0.0083 * 0.75, 0.3722 * 0.75)
    .lineTo(0.0083 * 0.75, 0.3202 * 0.75)
    .lineTo(0.0, 0.
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1558.stl