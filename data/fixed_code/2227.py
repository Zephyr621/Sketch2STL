import cadquery as cq
# --- Part 1: Door ---
# Define the outer loop points
outer_loop_points = [
    (0.0, 0.0),
    (0.75 * 0.75, 0.0),
    (0.75 * 0.75, 0.125 * 0.75),
    (0.625 * 0.75, 0.125 * 0.75)
]
# Define the inner loop points
inner_loop_points = [
    (0.5 * 0.75, 0.25 * 0.75),
    (0.5 * 0.75, 0.375 * 0.75),
    (0.625 * 0.75, 0.375 * 0.75),
    (0.625 * 0.75, 0.5 * 0.75)
]
# Create the outer loop
part_1 = cq.Workplane("XY")
# Create the outer loop
outer_loop = (
    part_1.moveTo(outer_loop_points[0][0], outer_loop_points[0][1])
    .lineTo(outer_loop_points[1][0], outer_loop_points[1][1])
    .lineTo(outer_loop_points[2][0], outer
# Export
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_2227.stl