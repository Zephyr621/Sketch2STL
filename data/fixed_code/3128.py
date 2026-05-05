import cadquery as cq
# --- Part 1: Rectangular Base ---
base_length = 0.75 * 0.75  # Scaled length
base_width = 0.1142 * 0.75  # Scaled width
base_height = 0.0193
part_1 = (
    cq.Workplane("XY")
    .rect(base_length, base_width)
    .extrude(base_height)
)
# --- Part 2: Holes ---
hole_radius = 0.0048 * 0.0857  # Scaled radius
hole_depth = 0.019
# Create the first hole
hole1_x = 0.0203 + 0.0048 * 0.0857
hole1_y = 0.0203 + 0.0048 * 0.0857
part_2 = (
    cq.Workplane("XY")
    .moveTo(hole1_x, hole1_y)
    .circle(hole_radius)
    .extrude(-hole_depth)
)
# Create the second hole
hole2_x = 0.7223 + 0.0048 * 0.0857
hole2_y = 0.0203 + 0.0048 * 0.0857
part_2 = (
    part_2.faces(">Z")
    .workplane()
    .moveTo(hole2_x, hole2_y)
    .circle(hole_radius)
    .cut
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3128.stl