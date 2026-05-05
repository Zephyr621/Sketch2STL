import cadquery as cq
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.1442 * 0.2842  # Sketch radius scaled
part_1_height = 0.75
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Part 2: Rectangular Cutout ---
part_2_length = 0.0312 * 0.0745
part_2_width = 0.0745 * 0.0745
part_2_height = 0.738
part_2 = (
    cq.Workplane("XY")
    .moveTo(0.0023 * 0.0745, 0.0023 * 0.0745)
    .lineTo(0.0288 * 0.0745, 0.0023 * 0.0745)
    .lineTo(0.0288 * 0.0745, 0.0851 * 0.0745)
    .threePointArc((0.0288 * 0.0745, 0.0469 * 0.0745), (0.0023 * 0.0745, 0.0851 * 0.0745))
    .close()
    .extrude(-part_2
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_3227.stl