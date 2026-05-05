import cadquery as cq
from cadquery import exporters
# --- Part 1: Rectangular Prism with Circular Hole ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.75 * 0.75   # Scaled width
part_1_height = 0.1875
hole_center_x = 0.375 * 0.75  # Scaled x-coordinate of hole center
hole_center_y = 0.3125 * 0.75  # Scaled y-coordinate of hole center
hole_radius = 0.1562 * 0.75   # Scaled radius
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
    .faces(">Z").workplane()
    .circle(hole_radius)
    .cutThruAll()
)
# --- Part 2: Cylinder ---
part_2_radius = 0.25 * 0.5  # Scaled radius
part_2_height = 0.5625
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(part_2_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0,
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_1532.stl