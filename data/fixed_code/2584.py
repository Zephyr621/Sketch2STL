import cadquery as cq
# --- Part 1 ---
outer_square_side = 0.75 * 0.75  # Scaled side length
inner_square_side = (0.6 - 0.3) * 0.75  # Scaled side length
height = 0.375
part_1 = (
    cq.Workplane("XY")
    .rect(outer_square_side, outer_square_side)
    .extrude(height)
    .cut(cq.Workplane("XY").rect(inner_square_side, inner_square_side).extrude(height))
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.375, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# Export to STL
cq.
cq.
cq.
cq.cq.exporters.export(
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2584.stl