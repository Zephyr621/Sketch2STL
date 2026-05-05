import cadquery as cq
# --- Part 1: Rectangular Beam ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.0312 * 0.075, 0.0)
    .lineTo(0.0312 * 0.075, 0.075 * 0.075)
    .lineTo(0.075 * 0.075, 0.075 * 0.075)
    .lineTo(0.075 * 0.075, 0.0078 * 0.075)
    .lineTo(0.0, 0.0078 * 0.075)
    .close()
    .extrude(0.75)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (1, 0, 0), -90)
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
# --- Part 2: Cutout ---
part_2 = (
    cq.Workplane("XY")
    .rect(0.0176 * 0.0625, 0.0625 * 0.0625)
    .extrude(-0.0625)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1835.stl