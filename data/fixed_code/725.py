import cadquery as cq
# --- Part 1: Box ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.4284 * 0.75  # Scaled width
part_1_height = 0.3127
inner_length = 0.7143 * 0.75
inner_width = 0.4286 * 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
    .cut(cq.Workplane("XY").rect(inner_length, inner_width).translate((0,0,part_1_height/2)).extrude(part_1_height + 0.1))
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.3127, 0))
# --- Part 2: Cube ---
part_2_size = 0.2812 * 0.5357  # Scaled size
part_2_height = 0.2143
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_size, part_2_size)
    .extrude
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_725.stl