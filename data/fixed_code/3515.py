import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cube with Circular Hole ---
part_1_size = 0.3214 * 0.3214  # Scaled size
part_1_height = 0.1607
part_1_hole_center_x = 0.1607 * 0.3214  # Scaled center x
part_1_hole_center_y = 0.1607 * 0.3214  # Scaled center y
part_1_hole_radius = 0.1071 * 0.3214  # Scaled radius
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_size, part_1_size)
    .extrude(-part_1_height)  # Extrude in the opposite direction for a hole
    .faces(">Z").workplane()
    .circle(part_1_hole_radius)
    .cutThruAll()
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.0536, 0.0536, 0))
# --- Part 2: Rectangular Plate with Curved Edges ---
part_2_length = 0.5357 * 0.75
part_2_width = 0.75 * 0.75
part_2_height = 0.2143
part_2 = (
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3515.stl