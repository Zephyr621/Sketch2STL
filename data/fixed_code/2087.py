import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Washer ---
part_1_outer_radius = 0.0393 * 0.0797  # Sketch radius scaled
part_1_inner_radius = 0.0446 * 0.0797  # Inner hole radius scaled
part_1_height = 0.0052
part_1 = (
    cq.Workplane("XY")
    .circle(part_1_outer_radius)
    .extrude(part_1_height)
    .cut(cq.Workplane("XY").circle(part_1_inner_radius).extrude(part_1_height))
)
# --- Part 2: Cylinder Cutout ---
part_2_outer_radius = 0.0149 * 0.0394  # Sketch radius scaled
part_2_inner_radius = 0.0446 * 0.0394  # Inner hole radius scaled
part_2_height = 0.0151
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_outer_radius)
    .extrude(-part_2_height)
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2087.stl