import cadquery as cq
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.0352 * 0.0703  # Sketch radius scaled
part_1_height = 0.75
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(-part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (1, 0, 0), -90)
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0.75, 0, 0))
# --- Part 2: Hexagonal Head ---
head_scale = 0.0281
head_height = 0.6346
head = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0062 * head_scale)
    .lineTo(0.0117 * head_scale, 0.0)
    .lineTo(0.0281 * head_scale, 0.0062 * head_scale)
    .lineTo(0.0281 * head_scale, 0.0281 * head_scale)
    .close()
    .extrude(head_height)
)
# --- Coordinate System Transformation for
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_453.stl