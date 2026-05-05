import cadquery as cq
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.0417 * 0.0833  # Sketch radius scaled
part_1_height = 0.75
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2: Cutout ---
part_2_width = 0.0375 * 0.0375
part_2_depth = 0.0188 * 0.0375
part_2_length = 0.0188 * 0.0375
part_2 = cq.Workplane("XY")
part_2 = part_2.moveTo(0, 0.0023 * 0.0375).lineTo(0.0375 * 0.0375, 0).lineTo(0.0375 * 0.0375, 0.0188 * 0.0375).lineTo(0, 0.0188 * 0.0375).close()
part_2 = part_2.moveTo(0, 0.0188 *
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_2977.stl