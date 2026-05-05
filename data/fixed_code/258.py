import cadquery as cq
from math import radians
# --- Part 1: Rectangular Object with Hole ---
part_1_length = 0.6818 * 0.6818  # Scaled length
part_1_width = 0.3409 * 0.6818   # Scaled width
part_1_height = 0.3409
hole_center_x = 0.3309 * 0.6818  # Scaled center x
hole_center_y = 0.1689 * 0.6818  # Scaled center y
hole_radius = 0.0352 * 0.6818   # Scaled radius
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
    .faces(">Z")
    .workplane()
    .circle(hole_radius)
    .cutThruAll()
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.3409, 0))
# --- Part 2: Cylinder with Hole ---
part_2_outer_radius = 0.375 * 0.75  # Scaled outer radius
part_2_inner_radius = 0.1714 * 0.75  # Scaled inner radius
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_258.stl