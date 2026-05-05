import cadquery as cq
from cadquery.vis import show
# --- Part 1: Rectangular Block with Curved Top and Hole ---
sketch_scale = 0.75
length = 0.75 * sketch_scale
width = 0.5625 * sketch_scale
height = 0.1406
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(length, 0.0)
    .threePointArc((length + (0.75 - 0.1875), 0.2812 * sketch_scale), (length, width))
    .lineTo(0.0, width)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(-height)
)
# Create the hole
hole_center_x = 0.375 * sketch_scale
hole_center_y = 0.3125 * sketch_scale
hole_radius = 0.0937 * sketch_scale
part_1 = part_1.faces(">Z").workplane().pushPoints([(hole_center_x - (length/2), hole_center_y - (width/2)]).hole(2 * hole_radius)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.1406, 0))
# --- Assembly ---
assembly =
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3545.stl