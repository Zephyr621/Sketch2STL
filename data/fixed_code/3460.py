import cadquery as cq
# --- Part 1 ---
outer_points = [
    (0.0, 0.6),
    (0.75, 0.6),
    (0.75, 0.625),
    (0.5625, 0.625),
    (0.5625, 0.75),
    (0.1875, 0.75)
]
inner_points = [
    (0.0562, 0.0234),
    (0.0562, 0.3281),
    (0.0234, 0.3281),
    (0.0234, 0.6495),
    (0.0562, 0.6495)
]
sketch_scale = 0.75
outer_points = [(x * sketch_scale, y * sketch_scale) for x, y in outer_points]
inner_points = [(x * sketch_scale, y * sketch_scale) for x, y in inner_points]
part_1 = (
    cq.Workplane("XY")
    .moveTo(outer_points[0][0], outer_points[0][1])
    .lineTo(outer_points[1][0], outer_points[1][1])
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3460.stl