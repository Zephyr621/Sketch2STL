import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Hexagonal Plate ---
part_1_scale = 0.75
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.3248 * part_1_scale)
    .lineTo(0.1875 * part_1_scale, 0.0)
    .lineTo(0.5625 * part_1_scale, 0.0)
    .lineTo(0.75 * part_1_scale, 0.3248 * part_1_scale)
    .lineTo(0.5625 * part_1_scale, 0.6495 * part_1_scale)
    .lineTo(0.1875 * part_1_scale, 0.6495 * part_1_scale)
    .lineTo(0.0, 0.3248 * part_1_scale)
    .close()
    .extrude(0.0547)
)
# --- Part 2: Rectangular Prism ---
part_2_scale = 0.6089
part_2_height = 0.1071
# Define the points for the hexagon
points = [
    (0.0, 0.0469),
    (0.1906 * part_2_scale, 0.0031),
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_562.stl