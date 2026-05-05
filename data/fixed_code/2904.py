import cadquery as cq
# --- Part 1: Rectangular Box with Cutout ---
outer_width = 0.75 * 0.75  # Scaled width
outer_height = 0.3 * 0.75  # Scaled height
inner_offset = 0.0094 * 0.75  # Scaled offset
depth = 0.3  # Depth of the extrusion (both directions)
# Create the outer rectangle
outer_rect = cq.Workplane("XY").rect(outer_width, outer_height).extrude(depth)
# Create the inner rectangle (cutout)
inner_rect = cq.Workplane("XY").rect(outer_width - 2 * inner_offset, outer_height - 2 * inner_offset).extrude(depth)
# Subtract the inner rectangle from the outer rectangle to create the cutout
part_1 = outer_rect.cut(inner_rect)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.3, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
#
# 定义结果变量
result = inner_rect
# 导出为STL文件
cq.exporters.export(result, "output_2904.stl