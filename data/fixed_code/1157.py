import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder ---
part_1_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_height = 0.375
circle1_center_x = 0.3562 * 0.75
circle1_center_y = 0.2589 * 0.75
circle2_center_x = 0.3695 * 0.75
circle2_center_y = 0.2274 * 0.75
circle3_center_x = 0.3562 * 0.75
circle3_center_y = 0.5714 * 0.75
circle4_center_x = 0.3562 * 0.75
circle4_center_y = 0.6286 * 0.75
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.1888 * 0.75, 0)
    .lineTo(0.5615 * 0.75, 0)
    .threePointArc((0.75 * 0.75, 0.1888 * 0.75), (0.5615 * 0.75, 0.2589 * 0.75))
    .lineTo(0.1888 * 0.75, 0.2589 * 0.75)
    .threePointArc((0, 0.1888 * 0.75), (0.1888 * 0.75
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1157.stl