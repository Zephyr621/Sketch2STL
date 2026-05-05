import cadquery as cq
from math import radians
# --- Part 1: Rectangular Box ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.2072 * 0.75  # Scaled width
part_1_height = 0.1875
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.1875, 0))
# --- Part 2: Cylinders (Cut Feature) ---
cylinder_radius = 0.0804 * 0.5556
cylinder_depth = 0.0234
cylinder_centers = [
    (0.0804 * 0.5556, 0.0804 * 0.5556),
    (0.0804 * 0.5556, 0.5759 * 0.5556),
    (0.6696 * 0.5556, 0.0804 * 0.5556),
    (0.6696 * 0.5556, 0.5759 *
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_272.stl