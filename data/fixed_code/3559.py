import cadquery as cq
from math import radians
# --- Part 1: Cylinder ---
part_1_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_height = 0.6
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(-part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Part 2: Hexagonal Cutout ---
sketch_scale_part2 = 0.65
hexagon_points = [
    (0.0 * sketch_scale_part2, 0.3248 * sketch_scale_part2),
    (0.3248 * sketch_scale_part2, 0.0 * sketch_scale_part2),
    (0.65 * sketch_scale_part2, 0.3248 * sketch_scale_part2),
    (0.6495 * sketch_scale_part2, 0.3248 * sketch_scale_part2),
    (0.6495 * sketch_scale_part2, 0.6495 * sketch_scale_part2),
]
part_2 = (
    cq.Workplane("XY")
    .polyline(hexagon_points)
    .close()
    .extrude(-0.6)
)
# Export
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_3559.stl