import cadquery as cq
# --- Part 1: Triangle Bracket ---
sketch_scale = 0.75
extrude_depth = 0.2497 * sketch_scale
# Scaled coordinates for the outer profile
outer_points = [
    (0.0, 0.4687 * sketch_scale),
    (0.375 * sketch_scale, 0.0),
    (0.75 * sketch_scale, 0.4687 * sketch_scale),
    (0.75 * sketch_scale, 0.5 * sketch_scale),
    (0.375 * sketch_scale, 0.5 * sketch_scale)
]
# Scaled coordinates for the inner profile
inner_points = [
    (0.0, 0.4687 * sketch_scale),
    (0.375 * sketch_scale, 0.0),
    (0.625 * sketch_scale, 0.4687 * sketch_scale),
    (0.625 * sketch_scale, 0.5 * sketch_scale),
    (0.125 * sketch_scale, 0.5 * sketch_scale),
    (0.125 * sketch_scale, 0.4687 * sketch_scale),
    (0.0, 0.4687 * sketch_scale)
]
# Create the outer profile using polygon
outer_profile =
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3412.stl