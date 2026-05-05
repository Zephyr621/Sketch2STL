import cadquery as cq
# --- Part 1: Triangular Prism ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.4688 * 0.5468, 0.0)
    .lineTo(0.4688 * 0.5468, 0.5468 * 0.5468)
    .lineTo(0.0, 0.5468 * 0.5468)
    .close()
    .extrude(0.75)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2: Rectangular Block (Cutout) ---
part_2 = (
    cq
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1369.stl