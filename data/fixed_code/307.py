import cadquery as cq
# --- Part 1: Cube with Rounded Edges ---
length = 0.75 * 0.75  # Scaled length
width = 0.375 * 0.75   # Scaled width
height = 0.5
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(length, 0.0)
    .lineTo(length, width)
    .lineTo(0.25 * 0.75, width)
    .lineTo(0.25 * 0.75, 0.125 * 0.75)
    .lineTo(0.5 * 0.75, 0.125 * 0.75)
    .lineTo(0.5 * 0.75, 0.375 * 0.75)
    .lineTo(0.25 * 0.75, 0.375 * 0.75)
    .lineTo(0.25 * 0.75, 0.125 * 0.75)
    .lineTo(0.0, 0.125 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0,
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_307.stl