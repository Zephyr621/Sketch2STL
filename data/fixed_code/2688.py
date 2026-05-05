import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder with Curved Top ---
sketch_scale = 0.75
# Scaled coordinates
start_point_arc1 = (0.0 * sketch_scale, 0.0893 * sketch_scale)
mid_point_arc1 = (0.375 * sketch_scale, 0.0309 * sketch_scale)
end_point_arc1 = (0.75 * sketch_scale, 0.0 * sketch_scale)
end_point_line1 = (0.6958 * sketch_scale, 0.0893 * sketch_scale)
mid_point_arc2 = (0.75 * sketch_scale, 0.3749 * sketch_scale)
end_point_arc2 = (0.7083 * sketch_scale, 0.3829 * sketch_scale)
extrude_depth = 0.3128
part_1 = (
    cq.Workplane("XY")
    .moveTo(start_point_arc1[0], start_point_arc1[1])
    .threePointArc(mid_point_arc1, end_point_arc1)
    .lineTo(end_point_line1[0], end_point_line1[1])
    .threePointArc(mid_point_arc
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2688.stl