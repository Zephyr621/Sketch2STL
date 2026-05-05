import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Base ---
part_1_length = 0.6857 * 0.6857  # Scaled length
part_1_width = 0.1737 * 0.6857  # Scaled width
part_1_height = 0.1737
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (1, 0, 0), -90)
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0.1737, 0, 0))
# --- Part 2: Cutout 1 ---
cutout_width = 0.0893 * 0.75
cutout_depth = 0.0146
cutout_1 = (
    cq.Workplane("XY")
    .moveTo(0,
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_269.stl