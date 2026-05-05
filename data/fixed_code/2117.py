import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.4357 * 0.436, 0.0)
    .lineTo(0.4357 * 0.436, 0.0117 * 0.436)
    .lineTo(0.2242 * 0.436, 0.0117 * 0.436)
    .lineTo(0.2242 * 0.436, 0.0235 * 0.436)
    .lineTo(0.1607 * 0.436, 0.0235 * 0.436)
    .lineTo(0.1607 * 0.436, 0.0)
    .lineTo(0.3188 * 0.436, 0.0)
    .lineTo(0.3188 * 0.436, 0.0235 * 0.436)
    .lineTo(0.0, 0.0235 * 0.436)
    .close()
    .extrude(0.75)
)
# --- Coordinate System Transformation
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2117.stl