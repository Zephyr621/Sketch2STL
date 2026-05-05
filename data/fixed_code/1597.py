import cadquery as cq
# --- Part 1: Rectangular Box with Cutout ---
outer_width = 0.75 * 0.75  # Scaled width
outer_length = 0.5357 * 0.75  # Scaled length
inner_offset = 0.0207 * 0.75  # Scaled offset for inner rectangle
height = 0.4813
part_1 = (
    cq.Workplane("XY")
    .rect(outer_width, outer_length)
    .extrude(height)
    .cut(cq.Workplane("XY").rect(outer_width - 2 * inner_offset, outer_length - 2 * inner_offset).extrude(height + 0.001)) # Extrude slightly more than the box's thickness
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.4813, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# Export to STL
cq.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1597.stl