import cadquery as cq
from math import radians
# --- Part 1: Rectangular Box ---
part_1_length = 0.5 * 0.75  # Scaled length
part_1_width = 0.75 * 0.75  # Scaled width
part_1_height = 0.3
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.3, 0))
# --- Part 2: Cut Feature ---
cut_depth = 0.225
cut_sketch = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.075 * 0.525)
    .lineTo(0.0, 0.45 * 0.525)
    .threePointArc((0.075 * 0.525, 0.45 * 0.525), (0.0, 0.075 * 0.525))
    .close()
)
cut_part = cut_sketch.extrude(-cut_depth)
# --- Coordinate System Transformation for Part 2 ---
cut_part = cut_
# Export
# 定义结果变量
result = cut_part
# 导出为STL文件
cq.exporters.export(result, "output_189.stl