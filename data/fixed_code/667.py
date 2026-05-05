import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Rectangular Block with Cutout ---
part_1_length = 0.7143 * 0.75  # Scaled length
part_1_width = 0.75 * 0.75   # Scaled width
part_1_height = 0.0536
cutout_x = 0.0829 * 0.75  # Scaled cutout x
cutout_y = 0.1786 * 0.75  # Scaled cutout y
cutout_size = (0.4286 - 0.0829) * 0.75  # Scaled cutout size
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
    .faces(">Z")
    .workplane()
    .rect(cutout_size, cutout_size)
    .cutThruAll()
)
# --- Part 2: Cylinder
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_667.stl