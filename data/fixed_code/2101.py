import cadquery as cq
from math import radians
# --- Part 1: Rectangular Block ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.1875 * 0.75  # Scaled width
part_1_height = 0.0625
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Part 2: Cylindrical Protrusions ---
cylinder_radius = 0.0469 * 0.0938  # Scaled radius
cylinder_height = 0.3125
# Cylinder positions relative to the part's coordinate system
cylinder_positions = [
    (0.0219 + 0.0469) * 0.0938 - part_1_length / 2, (0.0219 + 0.0938) * 0.0938 - part_1_width / 2, (0.0219 + 0.4687) * 0.0938 - part_1_width / 2,
    (0.0219 + 0.0469) * 0.0938 - part_1_length / 2, (0.0219 + 0.4687) * 0.0938 - part_1_width / 2,
]
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2101.stl