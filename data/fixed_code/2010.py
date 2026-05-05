import cadquery as cq
from cadquery import exporters
# --- Part 1: Cube with Circular Hole ---
part_1_size = 0.75 * 0.75  # Scaled size
part_1_height = 0.3
hole_radius = 0.15 * 0.75  # Scaled radius
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_size, part_1_size)
    .extrude(part_1_height)
    .faces(">Z")
    .workplane()
    .circle(hole_radius)
    .cutThruAll()
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.3, 0))
# --- Part 2: Cylinder with Hole ---
part_2_outer_radius = 0.15 * 0.3  # Scaled outer radius
part_2_inner_radius = 0.15 * 0.3  # Scaled inner radius
part_2_height = 0.3
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_outer_radius)
    .extrude(part_2_height)
    .faces(">Z")
    .workplane()
    .circle(part_2_inner
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2010.stl