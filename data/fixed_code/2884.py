import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.746 * 0.746, 0.0)
    .lineTo(0.746 * 0.746, 0.6429 * 0.746)
    .lineTo(0.0, 0.6429 * 0.746)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(-0.0075)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.2869, 0.0, 0.0))
# --- Part 2 ---
part_2 = (
    cq.Workplane("XY")
    .rect(0.746 * 0.746, 0.6429 * 0.746)
    .extrude(0.0075)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0.0, 0.0, 0.0))
# --- Part 3 ---
part_3 = (
    cq.Workplane("XY")
    .rect(0.746 * 0
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2884.stl