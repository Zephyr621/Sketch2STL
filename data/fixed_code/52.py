import cadquery as cq
from math import radians
# --- Part 1: Cylinder ---
part_1_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_height = 0.2812
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(-part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.2812, 0))
# --- Part 2: Hole ---
hole_radius = 0.2625 * 0.525
hole_depth = 0.0938
part_2 = cq.Workplane("XY").circle(hole_radius).extrude(-hole_depth)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.1875, 0, 0.1875))
# --- Part 3: Holes ---
hole_centers = [
    (0.1562, 0.0469),
    (0.1499, 0.0469),
    (0.1499, 0.5891),
    (0.1311, 0.0469),
# Export
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_52.stl