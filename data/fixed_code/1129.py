import cadquery as cq
from cadquery.vis import show
# --- Part 1: Rectangular Block with Triangular Cutout ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.375 * 0.75   # Scaled width
part_1_height = 0.15
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(part_1_length, 0)
    .lineTo(part_1_length, part_1_width)
    .lineTo(0.375 * 0.75, part_1_width)
    .lineTo(0, 0)
    .close()
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.3, 0))
# --- Part 2: Cylinder ---
part_2_radius = 0.3375 * 0.675  # Scaled radius
part_2_height = 0.075
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_radius)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1129.stl