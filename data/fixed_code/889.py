import cadquery as cq
from cadquery.vis import show
# --- Part 1: L-shaped CAD Model ---
sketch_scale = 0.75
extrude_depth = 0.0144 * sketch_scale
# Scaled dimensions
start_x1 = 0.0 * sketch_scale
end_x1 = 0.5381 * sketch_scale
mid_x1 = 0.75 * sketch_scale
mid_y1 = 0.0 * sketch_scale
end_x2 = 0.5381 * sketch_scale
end_y2 = 0.3267 * sketch_scale
center_x1 = 0.2513 * sketch_scale
center_x2 = 0.5381 * sketch_scale
center_y = 0.3267 * sketch_scale
radius1 = 0.0833 * sketch_scale
radius2 = 0.0417 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(start_x1, 0)
    .lineTo(end_x1, 0)
    .threePointArc((mid_x1, mid_y1), (end_x1, end_y2))
    .lineTo(start_x1, end_y2)
    .close()
    .
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_889.stl