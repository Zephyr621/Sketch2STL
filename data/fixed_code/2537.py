import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.0937 * 0.75)
    .lineTo(0.5208 * 0.75, 0.0937 * 0.75)
    .lineTo(0.5208 * 0.75, 0.1875 * 0.75)
    .lineTo(0.375 * 0.75, 0.1875 * 0.75)
    .lineTo(0.375 * 0.75, 0.0937 * 0.75)
    .lineTo(0.2812 * 0.75, 0.0937 * 0.75)
    .lineTo(0.2812 * 0.75, 0.1875 * 0.75)
    .lineTo(0.0, 0.1875 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(-0.1875)
)
# --- Coordinate System Transformation for Part 1 ---
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2537.stl