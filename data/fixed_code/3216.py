import cadquery as cq
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.2206 * 0.4473  # Sketch radius scaled
part_1_height = 0.3413
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(-part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.0785, 0.0785, 0.0))
# --- Part 2: Rectangular Block ---
part_2_width = 0.3904 * 0.3904
part_2_length = 0.3897 * 0.3904
part_2_height = 0.2785
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_width, part_2_length)
    .extrude(part_2_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_3216.stl