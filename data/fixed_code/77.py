import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder with Rectangular Cross-Section ---
sketch_scale = 0.4421
# Scaled Dimensions
start_x = 0.0 * sketch_scale
end_x = 0.4102 * sketch_scale
mid_y = 0.1607 * sketch_scale
height = 0.1879 * sketch_scale
extrude_depth = 0.75
# Create the rectangular profile
rect_profile = (
    cq.Workplane("XY")
    .moveTo(start_x, 0)
    .lineTo(end_x, 0)
    .threePointArc((0.2899 * sketch_scale, mid_y), (end_x, height))
    .lineTo(start_x, height)
    .close()
)
# Extrude the rectangle
part_1 = rect_profile.extrude(extrude_depth)
# Create the triangular cutout
cutout = (
    cq.Workplane("XY")
    .moveTo(start_x, height)
    .lineTo(end_x, height)
    .lineTo(end_x, 0)
    .lineTo(start_x, 0)
    .close()
    .extrude(extrude_depth)
)
# Subtract the
# Export
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_77.stl