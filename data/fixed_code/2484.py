import cadquery as cq
from cadquery import exporters
# --- Part 1: Cube with Opening ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.4261 * 0.4261, 0.0)
    .lineTo(0.4261 * 0.4261, 0.1071 * 0.4261)
    .lineTo(0.2143 * 0.4261, 0.1071 * 0.4261)
    .lineTo(0.2143 * 0.4261, 0.4261 * 0.4261)
    .lineTo(0.0, 0.4261 * 0.4261)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(-0.75)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Part 2: Cylinder ---
part_2_radius = 0.0234 * 0.0469  # Sketch radius scaled
part_2_height = 0.25
part_2 = (
    cq.Workplane("XY")
    .workplane(offset=0.75)
    .moveTo(0.00
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2484.stl