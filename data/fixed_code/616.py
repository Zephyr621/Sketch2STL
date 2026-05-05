import cadquery as cq
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.25 * 0.5  # Sketch radius scaled
part_1_height = 0.125
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.125, 0.125, 0.125))
# --- Part 2: Triangular Prism ---
part_2_scale = 0.25
part_2 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.25 * part_2_scale, 0.0)
    .lineTo(0.25 * part_2_scale, 0.125 * part_2_scale)
    .lineTo(0.0, 0.125 * part_2_scale)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(-0.375)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), 180)
part_2 = part_2.translate((0
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_616.stl