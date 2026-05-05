import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cube with Circular Hole ---
part_1_size = 0.5115 * 0.5115  # Scaled size
part_1_hole_radius = 0.1172 * 0.5115  # Scaled radius
part_1_height = 0.2582
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_size, part_1_size)
    .extrude(part_1_height)
    .faces(">Z")
    .workplane()
    .circle(part_1_hole_radius)
    .cutThruAll()
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2: Cylinder ---
part_2_radius = 0.0937 * 0.1941  # Scaled radius
part_2_height = 0.375
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_radius)
    .extrude(part_2_height)
)
# --- Coordinate System Transformation
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2094.stl