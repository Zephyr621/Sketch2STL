import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Rectangular Object with Cutout ---
sketch_scale_part1 = 0.75
length_part1 = 0.75 * sketch_scale_part1
width_part1 = 0.585 * sketch_scale_part1
height_part1 = 0.0019
# Create the base shape with cutouts
base_shape = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(length_part1, 0.0)
    .lineTo(length_part1, width_part1)
    .lineTo(0.0, width_part1)
    .close()
)
# Extrude the base shape to create the solid
part_1 = base_shape.extrude(height_part1)
# Create the hole
hole_center_x = 0.3746 * sketch_scale_part1
hole_center_y = 0.2709 * sketch_scale_part1
hole_radius = 0.0134 * sketch_scale_part1
part_1 = (
    part_1.faces(">Z")
    .workplane()
    .hole(2 * hole_radius)
)
# --- Part 2: Cylinder Cutout ---
sketch_
# Export
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_1600.stl