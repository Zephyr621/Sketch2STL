import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.4504 * sketch_scale
# Scaled circle parameters
circle1_center = (0.1875 * sketch_scale, 0.3248 * sketch_scale)
circle2_center = (0.5625 * sketch_scale, 0.325 * sketch_scale)
circle3_center = (0.375 * sketch_scale, 0.6495 * sketch_scale)
circle4_center = (0.5882 * sketch_scale, 0.3248 * sketch_scale)
part_1 = (
    cq.Workplane("XY")
    .moveTo(circle1_center[0], circle1_center[1])
    .circle(circle1_radius)
    .moveTo(circle2_center[0], circle2_center[1])
    .circle(circle2_radius)
    .moveTo(circle3_center[0], circle3_center[1])
    .circle(circle3_radius)
    .moveTo(circle4_center[0], circle4_center[1])
    .circle(circle4_radius)
    .extrude(extr
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3257.stl