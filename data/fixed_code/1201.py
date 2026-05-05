import cadquery as cq
# --- Part 1: Rectangular Prism ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.3243 * 0.75  # Scaled width
part_1_height = 0.0101
part_1 = cq.Workplane("XY").rect(part_1_length, part_1_width).extrude(part_1_height)
# --- Part 2: Cylindrical Holes ---
hole_radius = 0.0078 * 0.5644  # Scaled radius
hole_depth = 0.0101
# Hole centers (scaled and translated)
hole1_x = 0.0144 + 0.0144
hole1_y = 0.0144 + 0.0144
hole2_x = 0.0144 + 0.4964 - 0.0144
hole2_y = 0.0144 + 0.0144
part_2 = (
    cq.Workplane("XY")
    .pushPoints([(hole1_x, hole1_y), (hole2_x, hole2_y)])
    .circle(hole_radius)
    .extrude(-hole_depth)
)
# --- Assembly: Cut Holes from Base ---
assembly = part_1.cut(part_2.translate((0.0938, 0.0307, part_1_height)))
# Export
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_1201.stl