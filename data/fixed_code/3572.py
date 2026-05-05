import cadquery as cq
from math import radians
# --- Part 1: Cube with Circular Hole ---
cube_size = 0.75 * 0.75  # Scaled cube size
hole_radius = 0.1406 * 0.75  # Scaled hole radius
extrude_depth = 0.375
part_1 = (
    cq.Workplane("XY")
    .rect(cube_size, cube_size)
    .extrude(extrude_depth)
    .faces(">Z")
    .workplane()
    .circle(hole_radius)
    .cutThruAll()
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.375, 0))
# --- Part 2: Cylindrical Holes ---
hole_radius = 0.2812 * 0.5625  # Scaled hole radius
extrude_depth = 0.2812
hole_centers = [
    (0.2812 * 0.5625, 0.2812 * 0.5625),
    (0.2812 * 0.5625, 0.2812 * 0.5625),
    (0.2812 * 0.5625, 0.4687 * 0.5625),
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3572.stl