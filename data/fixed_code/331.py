import cadquery as cq
from cadquery import exporters
# --- Part 1: L-shaped base ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.2761 * 0.75)
    .lineTo(0.2812 * 0.75, 0.2761 * 0.75)
    .lineTo(0.2812 * 0.75, 0.4057 * 0.75)
    .lineTo(0.0, 0.4057 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.1869)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.1869, 0))
# --- Part 2: Cylindrical Section (Cutout) ---
part_2_radius = 0.1382 * 0.2344
part_2_height = 0.1869
part_2 = (
    cq.Workplane("XY")
    .workplane()
    .circle(part_2_radius)
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_331.stl