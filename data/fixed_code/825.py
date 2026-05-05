import cadquery as cq
from cadquery import exporters
# --- Part 1: Cube with Circular Hole ---
part_1_size = 0.6429 * 0.6429  # Scaled size
part_1_height = 0.1071
part_1_hole_radius = 0.0536 * 0.6429
part_1_extrude_depth = 0.6071
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_size, part_1_size)
    .extrude(part_1_extrude_depth)
    .faces(">Z").workplane()
    .circle(part_1_hole_radius)
    .cutThruAll()
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0.0434, 0.75, 0))
# --- Part 2: Cylinder ---
part_2_radius = 0.375 * 0.75  # Scaled radius
part_2_height = 0.3746
part_2_x_offset = 0.0434
part_2_y_offset = 0.0434
part_2_z_offset = 0.1071
part_2 = (
    cq.Workplane("
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_825.stl