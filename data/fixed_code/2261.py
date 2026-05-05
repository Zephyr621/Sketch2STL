import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder ---
part_1_radius = 0.0134 * 0.0278  # Sketch radius scaled
part_1_height = 0.75
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2: Holes ---
hole_radius = 0.0054 * 0.0278
hole_depth = 0.0429
hole_locations = [
    (0.0054 * 0.0278, 0.0054 * 0.0278),
    (0.0054 * 0.0278, 0.0208 * 0.0278),
    (0.0266 * 0.0278, 0.0054 * 0.0278),
    (0.0266 * 0.0278, 0.0208 * 0.0278)
]
# Create holes using arcs
for x, y in hole_locations:
    part_1 = part_1.faces(">Z").workplane().pushPoints([(x - (0.0134/0.0278)*0.0278, y - (0.0134/0.02
# Export
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_2261.stl