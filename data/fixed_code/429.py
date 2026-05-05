import cadquery as cq
from cadquery import exporters
# --- Part 1: Cube with Circular Hole ---
part_1_size = 0.5 * 0.5  # Scaled size
part_1_hole_radius = 0.15 * 0.5  # Scaled radius
part_1_extrude_depth = 0.5
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_size, part_1_size)
    .extrude(-part_1_extrude_depth)
    .faces(">Z")
    .workplane()
    .circle(part_1_hole_radius)
    .cutThruAll()
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0.125, 0, 0))
# --- Part 2: Cut Feature ---
part_2_size = 0.25 * 0.25  # Scaled size
part_2_height = 0.3
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_size, part_2_size)
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_429.stl