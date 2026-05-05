import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.2709 * 2  # Total extrusion depth (towards + opposite normal)
# Scaled coordinates for the outer profile
outer_points = [
    (0.0, 0.375),
    (0.1607 * sketch_scale, 0.0),
    (0.4818 * sketch_scale, 0.0),
    (0.4818 * sketch_scale, 0.75 * sketch_scale),
    (0.0, 0.75 * sketch_scale),
    (0.0, 0.375)
]
# Scaled circle parameters
circle1_center = (0.3047 * sketch_scale, 0.5114 * sketch_scale)
circle2_center = (0.3047 * sketch_scale, 0.6636 * sketch_scale)
circle_radius = 0.0547 * sketch_scale
# Create the base rectangle
part_1 = (
    cq.Workplane("XY")
    .moveTo(outer_points[0][0], outer_points[0][1])
    .lineTo(outer_points[1][0], outer_points[1][1])
    .threePointArc((0.2499 * sketch_scale
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2369.stl