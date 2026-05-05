import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Rectangular Plate ---
part_1_length = 0.5 * 0.5  # Scaled length
part_1_width = 0.3333 * 0.5  # Scaled width
part_1_height = 0.0133
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.25, 0.0873, 0))
# --- Part 2: Cylinders ---
cylinder_radius = 0.0867 * 0.3333
cylinder_depth = 0.0375
cylinder_centers = [
    (0.0867 * 0.3333 - 0.0867 * 0.3333, 0.0867 * 0.3333 - 0.0867 * 0.3333),
    (0.0867 * 0.3333 - 0.0867 * 0.3333, 0.0867 * 0.3333 - 0.0867 * 0.3333),
    (0.4167 * 0.3333 - 0.0867 * 0.3333,
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_670.stl