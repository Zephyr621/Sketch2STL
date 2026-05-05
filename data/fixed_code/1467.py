import cadquery as cq
from math import radians
# --- Part 1: Cylinder ---
part_1_radius = 0.0479 * 0.0907  # Sketch radius scaled
part_1_height = 0.75
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2: Curved Top ---
sketch_scale_part2 = 0.0293
part_2_points = [
    (0.0, 0.0061),
    (0.0061, 0.0),
    (0.0293, 0.0),
    (0.0293, 0.0197),
    (0.0061, 0.0197),
]
part_2 = (
    cq.Workplane("XY")
    .polyline(part_2_points)
    .close()
    .extrude(-0.0293)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0,
# Export
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_1467.stl