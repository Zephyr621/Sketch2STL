import cadquery as cq
from cadquery import exporters
# --- Part 1: Rectangular Bar ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.0155 * 0.75  # Scaled width
part_1_height = 0.0083
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)  # Extrude in the opposite direction
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Part 2: Cut Feature (Circles) ---
cut_radius = 0.0417 * 0.5446  # Scaled radius
cut_depth = 0.0033
# Create the cutting circles and position them using the provided positions
cut
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2005.stl