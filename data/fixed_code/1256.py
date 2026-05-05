import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Cube with Hole ---
part_1_size = 0.75 * 0.75  # Scaled size
part_1_hole_radius = 0.1262 * 0.75  # Scaled radius
part_1_extrude = 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_size, part_1_size)
    .extrude(part_1_extrude)
    .faces(">Z").workplane()
    .circle(part_1_hole_radius)
    .cutThruAll()
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2: Protruding Rectangular Section ---
part_2_size = 0.75 * 0.75  # Scaled size
part_2_height = 0.75
part_2 = (
    cq.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1256.stl