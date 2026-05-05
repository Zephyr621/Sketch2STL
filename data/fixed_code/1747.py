import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.0833 * 0.0833, 0.0)
    .lineTo(0.0833 * 0.0833, 0.0833 * 0.0833)
    .lineTo(0.0267 * 0.0833, 0.0833 * 0.0833)
    .lineTo(0.0267 * 0.0833, 0.0)
    .lineTo(0.75 * 0.0833, 0.0)
    .lineTo(0.75 * 0.0833, 0.0833 * 0.0833)
    .lineTo(0.5167 * 0.0833, 0.0833 * 0.0833)
    .lineTo(0.5167 * 0.0833, 0.0833 * 0.0833)
    .lineTo(0.0833 * 0.0833, 0.0833 * 0.0833)
    .lineTo(0.0833 * 0.0833, 0.0833 * 0.0833)
    .lineTo(0.0, 0.0833 * 0.0833)
    .lineTo(0.0, 0.0)
    .
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1747.stl