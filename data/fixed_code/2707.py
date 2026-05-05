import cadquery as cq
from math import radians
# --- Part 1: Cylinder ---
part_1_radius = 0.1364 * 0.2763  # Sketch radius scaled
part_1_height = 0.5921
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(-part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.0462, 0.0462, 0))
# --- Part 2: Cutout ---
part_2_outer_radius = 0.2308 * 0.4656
part_2_inner_radius = 0.1154 * 0.4656
part_2_height = 0.1705
part_2 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.4656 * 0.4656, 0.0)
    .threePointArc((0.375 * 0.4656, 0.1364 * 0.4656), (0.4656 * 0.4656, 0.4656 * 0.4656))
    .lineTo(0.0, 0.4656 * 0.4656)
    .
# Export
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_2707.stl