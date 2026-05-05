import cadquery as cq
# --- Part 1 ---
outer_points = [
    (0.0, 0.0),
    (0.75 * 0.75, 0.0),
    (0.75 * 0.75, 0.125 * 0.75),
    (0.625 * 0.75, 0.125 * 0.75),
    (0.625 * 0.75, 0.25 * 0.75)
]
inner_points = [
    (0.0375 * 0.75, 0.0375 * 0.75),
    (0.7125 * 0.75, 0.0375 * 0.75),
    (0.7125 * 0.75, 0.25 * 0.75),
    (0.0, 0.25 * 0.75)
]
part_1 = (
    cq.Workplane("XY")
    .polyline(outer_points)
    .close()
    .polyline(inner_points)
    .close()
    .extrude(0.375)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2487.stl