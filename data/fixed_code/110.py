import cadquery as cq
from math import radians
# --- Part 1: Rectangular Tag with Rounded Ends ---
sketch_scale = 0.75
extrude_depth = 0.1268 * 2  # Total extrusion depth (towards + opposite normal)
# Scaled dimensions
start_x1 = 0.1537 * sketch_scale
end_x1 = 0.5389 * sketch_scale
mid_arc1 = 0.75 * sketch_scale
mid_arc2 = 0.375 * sketch_scale
center_x1 = 0.6151 * sketch_scale
center_y1 = 0.1486 * sketch_scale
center_x2 = 0.75 * sketch_scale
center_y2 = 0.1486 * sketch_scale
radius = 0.0767 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(start_x1, 0)
    .lineTo(end_x1, 0)
    .threePointArc((mid_arc1, mid_arc1), (end_x1, end_y1))
    .lineTo(start_x1, end_y1)
    .threePointArc((0, mid_arc1), (start_x1, 0))
    .close()
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_110.stl