import cadquery as cq
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.0335 * 0.0507  # Sketch radius scaled
part_1_height = 0.75
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2: Cutout ---
cutout_wp = cq.Workplane("XY")
# Define the points for the cutout
points = [
    (0.0, 0.0448),
    (0.0357, 0.0),
    (0.0357, 0.0448),
    (0.0448, 0.0448),
]
# Scale the points
scaled_points = [(x * 0.0448, y * 0.0448) for x, y in points]
# Create the cutout profile
cutout = (
    cutout_wp
    .polyline(scaled_points)
    .close()
    .extrude(-
# 定义结果变量
result = cutout_wp
# 导出为STL文件
cq.exporters.export(result, "output_439.stl