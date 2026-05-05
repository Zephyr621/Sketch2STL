import cadquery as cq
# --- Part 1: Triangular Cutout ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.3404 * 0.75, 0.0)
    .lineTo(0.3404 * 0.75, 0.75 * 0.75)
    .lineTo(0.0, 0.75 * 0.75)
    .close()
    .extrude(-0.0851)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
# --- Part 2: Rectangular Block Cutout ---
part_2 = (
    cq.Workplane("XY")
    .rect(0.3214 * 0.3214, 0.2411 * 0.3214)
    .extrude(-0.15)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0.1365, 0.
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3076.stl