import cadquery as cq
# --- Part 1: Rectangular Object with Hole ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.25 * 0.75   # Scaled width
part_1_height = 0.0333 * 2  # Total height (both directions)
hole_center_x = 0.375 * 0.75  # Scaled x position of the hole center
hole_center_y = 0.0625 * 0.75  # Scaled y position of the hole center
hole_radius = 0.0312 * 0.75  # Scaled radius
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
    .faces(">Z").workplane()
    .moveTo(hole_center_x - part_1_length/2, hole_center_y - part_1_width/2)
    .circle(hole_radius)
    .cutThruAll()
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.1367, 0))
# --- Part 2: Rectangular Block ---
part_2_length = 0.75 * 0.75  #
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2758.stl