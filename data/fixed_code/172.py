import cadquery as cq
# --- Part 1: L-shaped base ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.25 * 0.625, 0.0)
    .lineTo(0.25 * 0.625, 0.625 * 0.625)
    .lineTo(0.5 * 0.625, 0.625 * 0.625)
    .lineTo(0.5 * 0.625, 0.25 * 0.625)
    .lineTo(0.25 * 0.625, 0.25 * 0.625)
    .lineTo(0.25 * 0.625, 0.625 * 0.625)
    .lineTo(0.0, 0.625 * 0.625)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.75)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2: Cube with rounded edges ---
cube_size = 0.25 * 0.25  # Sketch size scaled
cube_height = 0.375
part_2 = (
    cq.Workplane
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_172.stl