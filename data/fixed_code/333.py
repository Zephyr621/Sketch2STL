import cadquery as cq
from cadquery import exporters
# --- Part 1: Pentagon Base ---
part_1_points = [
    (0.0, 0.5756),
    (0.1572, 0.0),
    (0.5938, 0.5756)
]
part_1_points_scaled = [(x * 0.75, y * 0.75) for x, y in part_1_points]
part_1 = (
    cq.Workplane("XY")
    .polyline(part_1_points_scaled)
    .close()
    .extrude(0.2287)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.2287, 0))
# --- Part 2: Rectangular Cutout ---
part_2_width = 0.2409 * 0.3889
part_2_height = 0.3889 * 0.3889
part_2_depth = 0.0395
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_width, part_2_height)
    .extrude
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_333.stl