import cadquery as cq
# --- Part 1: Base with Circular Hole ---
part_1_length = 0.6 * 0.6  # Scaled length
part_1_width = 0.6 * 0.6  # Scaled width
part_1_height = 0.6
hole_center_x = 0.15 * 0.6  # Scaled center x
hole_center_y = 0.3 * 0.6  # Scaled center y
hole_radius = 0.225 * 0.6  # Scaled radius
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
    .faces(">Z").workplane()
    .circle(hole_radius)
    .cutThruAll()
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2: Cutout Cube ---
part_2_size = 0.3 * 0.5  # Scaled size
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3339.stl