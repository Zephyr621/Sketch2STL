import cadquery as cq
# --- Part 1: Rectangular Object with Cutout ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.3438 * 0.75)
    .lineTo(0.7188 * 0.75, 0.3438 * 0.75)
    .lineTo(0.7188 * 0.75, 0.5581 * 0.75)
    .lineTo(0.0, 0.5581 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(-0.0156)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Part 2: Rectangular Block ---
part_2 = (
    cq.Workplane("XY")
    .rect(0.02125 * 0.0212, 0.0156
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_89.stl