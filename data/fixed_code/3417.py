import cadquery as cq
# --- Part 1: Rectangular Plate with Circular Hole ---
plate_length = 0.75 * 0.75  # Scaled length
plate_width = 0.4423 * 0.75  # Scaled width
plate_height = 0.1867
hole_center_x = 0.375 * 0.75  # Scaled x-coordinate
hole_center_y = 0.2194 * 0.75  # Scaled y-coordinate
hole_radius = 0.0214 * 0.75  # Scaled radius
part_1 = (
    cq.Workplane("XY")
    .rect(plate_length, plate_width)
    .extrude(plate_height)
    .faces(">Z")
    .workplane()
    .moveTo(hole_center_x - plate_length/2, hole_center_y - plate_width/2)
    .circle(hole_radius)
    .cutThruAll()
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.1867, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3417.stl