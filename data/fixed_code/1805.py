import cadquery as cq
# --- Part 1: Cube with Corner Cut Off ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.3214 * 0.75)
    .lineTo(0.3172 * 0.75, 0.3214 * 0.75)
    .lineTo(0.1516 * 0.75, 0.3214 * 0.75)
    .lineTo(0.75 * 0.75, 0.3214 * 0.75)
    .lineTo(0.75 * 0.75, 0.6429 * 0.75)
    .lineTo(0.4687 * 0.75, 0.6429 * 0.75)
    .lineTo(0.4687 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.3214 * 0.75)
    .lineTo(0.0, 0.3214 * 0.75)
    .close()
    .extrude(0.1071)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1805.stl