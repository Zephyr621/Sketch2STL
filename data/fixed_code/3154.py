import cadquery as cq
# --- Part 1: Rectangular Prism with Cylindrical Hole ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.375 * 0.75  # Scaled width
part_1_height = 0.1875 + 0.1875  # Total extrusion depth
hole_center_x = 0.375 * 0.75  # Scaled center x
hole_center_y = 0.2187 * 0.75  # Scaled center y
hole_radius = 0.0937 * 0.75  # Scaled radius
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
    .faces(">Z")
    .workplane()
    .moveTo(hole_center_x - part_1_length/2, hole_center_y - part_1_width/2)
    .circle(hole_radius)
    .cutThruAll()
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.1875, 0))
# --- Assembly ---
assembly = part_1
# --- Export to STL ---
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3154.stl