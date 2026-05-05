import cadquery as cq
from math import radians
# --- Part 1: Cube ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.0764 * 0.75  # Scaled width
part_1_height = 0.0069
part_1 = cq.Workplane("XY").rect(part_1_length, part_1_width).extrude(-part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
# --- Part 2: Holes ---
hole_radius = 0.0104 * 0.0286  # Scaled radius
hole_depth = 0.0312
# Define hole positions relative to part_1's coordinate system
hole_positions = [
    (0.0104 * 0.0286 + 0.0104 * 0.0286, 0.0104 * 0.0286 + 0.0104 * 0.0286),  # Bottom Left
    (0.0104 * 0.0286 + 0.0286 * 0.0286, 0.0104 * 0.0286 + 0.0104 * 0.0286),  # Top Right
    (0.7332 * 0.0286 + 0.0104
# Export
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_1031.stl