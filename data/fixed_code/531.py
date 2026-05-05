import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder ---
sketch_scale = 0.75
extrude_depth = 0.0286 * 2  # Total extrusion depth (towards + opposite)
# Scaled dimensions
arc_start_x = 0.3743 * sketch_scale
arc_start_y = 0.2771 * sketch_scale
arc_mid_x = 0.375 * sketch_scale
arc_mid_y = 0.75 * sketch_scale
arc_end_x = 0.3743 * sketch_scale
arc_end_y = 0.2771 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, arc_start_y)
    .threePointArc((arc_mid_x, arc_mid_y), (arc_end_x, arc_end_y))
    .lineTo(0.0, arc_start_y)
    .close()
    .extrude(extrude_depth)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_531.stl