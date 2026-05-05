import cadquery as cq
from math import *
# --- Part 1: Rectangular Plate with Holes ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.4686 * 0.75  # Scaled width
part_1_height = 0.0469
hole_radius_small = 0.0274 * 0.75  # Scaled radius
hole_radius_large = 0.0635 * 0.75  # Scaled radius
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
    .faces(">Z")
    .workplane()
    .pushPoints([
        (0.0469 * 0.75 - part_1_length/2, 0.0469 * 0.75 - part_1_width/2),
        (0.0469 * 0.75 - part_1_length/2, 0.6261 * 0.75 - part_1_width/2)
    ])
    .hole(2 * hole_radius_small)
)
# --- Part 2: Cube ---
part_2_size = 0.6711 * 0.6711  # Scaled size
part_2_depth = 0.
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1156.stl