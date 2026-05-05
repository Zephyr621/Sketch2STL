import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Base ---
part_1_scale = 0.75
part_1_depth = 0.15
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(0.6 * part_1_scale, 0)
    .threePointArc((0.75 * part_1_scale, 0.375 * part_1_scale), (0.6 * part_1_scale, 0.3 * part_1_scale))
    .lineTo(0, 0.3 * part_1_scale)
    .close()
    .extrude(part_1_depth)
)
# Cut out the central hole
part_1 = (
    part_1.faces(">Z")
    .workplane()
    .circle(0.075 * part_1_scale)
    .cutThruAll()
)
# Create the three cylinders
cylinder_radius = 0.1125 * part_1_scale
cylinder_centers = [
    (0.1125 * part_1_scale, 0.1125 * part_1_scale),
    (0.1125 * part
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_222.stl