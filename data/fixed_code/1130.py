import cadquery as cq
from cadquery import exporters
# --- Part 1: Rectangular Box ---
part_1_length = 0.2701 * 0.5391  # Scaled length
part_1_width = 0.5391 * 0.5391   # Scaled width
part_1_height = 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)  # Extrude in the opposite direction for cutting
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Part 2: Cylindrical Protrusions ---
cylinder_radius = 0.0682 * 0.4375
cylinder_height = 0.1304
cylinder1 = cq.Workplane("XY").circle(cylinder_radius).extrude(cylinder_height)
cylinder2 = cq.Workplane("XY").circle(cylinder_radius).extrude(cylinder_height)
# --- Coordinate System Transformation for Cylinder 1 ---
cylinder1 = cylinder1.rotate((0, 0, 0), (1, 0, 0), -90)
cylinder1 = cylinder1.rotate((0, 0
# 定义结果变量
result = cylinder2
# 导出为STL文件
cq.exporters.export(result, "output_1130.stl