import cadquery as cq
# --- Part 1: Rectangular Prism with Holes ---
length = 0.75 * 0.75  # Scaled length
width = 0.0457 * 0.75  # Scaled width
height = 0.0577
hole_radius = 0.0086 * 0.75  # Scaled radius
hole1_x = 0.0261 * 0.75  # Scaled x position
hole2_x = 0.7083 * 0.75  # Scaled y position
hole_y = 0.0352 * 0.75  # Scaled y position
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
    .faces(">Z")
    .workplane()
    .pushPoints([(hole1_x - length/2, hole_y - width/2), (hole2_x - length/2, hole_y - width/2)])
    .hole(2 * hole_radius)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0577, 0))
# --- Assembly ---
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1257.stl