import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder with Rounded Edges ---
sketch_scale = 0.75
extrude_depth = 0.0094 * sketch_scale
# Scaled coordinates for the sketch
start_point1 = (0.0548 * sketch_scale, 0.1364 * sketch_scale)
mid_point1 = (0.375 * sketch_scale, 0.0)
end_point1 = (0.6958 * sketch_scale, 0.4773 * sketch_scale)
start_point2 = (0.6958 * sketch_scale, 0.4773 * sketch_scale)
mid_point2 = (0.75 * sketch_scale, 0.7083 * sketch_scale)
end_point2 = (0.6958 * sketch_scale, 0.75 * sketch_scale)
start_point3 = (0.0548 * sketch_scale, 0.75 * sketch_scale)
mid_point3 = (0.0 * sketch_scale, 0.7083 * sketch_scale)
end_point3 = (0.0548 * sketch_scale, 0.4773 * sketch_scale)
center_x = 0.375 * sketch_scale
center_y = 0.3544 * sketch_scale
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2984.stl