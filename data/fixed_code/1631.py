import cadquery as cq
# --- Part 1: Cube with L-shaped cutout ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.2344)
    .lineTo(0.5, 0.2344)
    .lineTo(0.5, 0.4687)
    .lineTo(0.25, 0.4687)
    .lineTo(0.25, 0.2344)
    .lineTo(0.0, 0.2344)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.375 * 0.75)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.375, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1631.stl