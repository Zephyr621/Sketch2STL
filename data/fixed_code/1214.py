import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Rectangular Base with Rounded Corners ---
sketch_scale = 0.75
extrude_depth = 0.0833 * sketch_scale
width = 0.75 * sketch_scale
length = 0.5 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(length, 0)
    .threePointArc((length + 0.125 * sketch_scale, 0), (length, width))
    .lineTo(0, width)
    .lineTo(0, 0)
    .close()
    .extrude(extrude_depth)
)
# Create the rounded corner
corner_radius = min(length, width) / 10  # Adjust radius as needed
part_1 = part_1.edges("|Z").fillet(corner_radius)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0833 * sketch_scale, 0))
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1214.stl