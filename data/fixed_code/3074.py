import cadquery as cq
from math import radians
# --- Part 1: Semi-circular Shape ---
part_1_scale = 0.75
part_1_depth = 0.0086 * 2  # Total depth (towards + opposite normal)
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(0.75 * part_1_scale, 0)
    .threePointArc((0.7382 * part_1_scale, 0.1934 * part_1_scale), (0.3727 * part_1_scale, 0))
    .lineTo(0.3727 * part_1_scale, 0.3813 * part_1_scale)
    .lineTo(0.0, 0.3813 * part_1_scale)
    .close()
    .extrude(part_1_depth)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.0469))
# --- Part 2: Cylinder ---
part_2_scale = 0.75
part_2_radius = 0.3567 * part_2_scale
part_2_height = 0.0703 * 2  # Total height (towards + opposite normal)
part_2 = (
    cq.Workplane("XY")
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3074.stl