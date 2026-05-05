import cadquery as cq
from cadquery.vis import show
# --- Part 1: Base with Cutout ---
part_1_length = 0.75 * 0.75
part_1_width = 0.5357 * 0.75
part_1_height = 0.2143
hole_center_x = 0.375 * 0.75
hole_center_y = 0.2614 * 0.75
hole_radius = 0.0714 * 0.75
base_cutout_x = 0.3214 * 0.75
base_cutout_y = 0.2571 * 0.75
base = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(part_1_length, 0)
    .lineTo(part_1_length, part_1_width)
    .lineTo(0, part_1_width)
    .close()
    .extrude(part_1_height)
)
# Create the hole
hole = (
    cq.Workplane("XY")
    .moveTo(hole_center_x, hole_center_y)
    .circle(hole_radius)
    .extrude(part_1_
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_424.stl