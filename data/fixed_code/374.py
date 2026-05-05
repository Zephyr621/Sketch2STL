import cadquery as cq
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.3045 * 0.7125  # Sketch radius scaled
part_1_height = 0.1518 + 0.1518
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.2917, 0))
# --- Part 2: Hexagonal Base ---
hex_scale = 0.75
hex_height = 0.1312 + 0.1312
hexagon = cq.Workplane("XY").polyline([(x * hex_scale, y * hex_scale) for x, y in [(0.0937 * hex_scale, 0.2812 * hex_scale), (0.4688 * hex_scale, 0.0937 * hex_scale)]]).close().extrude(hex_height)
# --- Coordinate System Transformation for Part 2 ---
hexagon = hexagon.rotate((0, 0, 0), (0, 0, 1), -90)
hexagon = hexagon.translate((0.0438, 0.1312, 0.0438
# 定义结果变量
result = hexagon
# 导出为STL文件
cq.exporters.export(result, "output_374.stl