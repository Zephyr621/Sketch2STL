import cadquery as cq
# --- Part 1: Rectangular Prism ---
part_1_width = 0.2188 * 0.75  # Sketch width scaled
part_1_height = 0.75 * 0.75 # Sketch height scaled
part_1_depth = 0.00312 + 0.00312
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_width, part_1_height)
    .extrude(part_1_depth)
)
# --- Part 2: Vertical Extension ---
part_2_width = 0.1875 * 0.375  # Sketch width scaled
part_2_height = 0.375 * 0.375  # Sketch height scaled
part_2_depth = 0.0075
part_2 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(part_2_width, 0)
    .lineTo(part_2_width, part_2_height)
    .lineTo(0, part_2_height)
    .close()
    .extrude(part_2_depth)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0.0938, 0, 0))
# --- Assembly ---
assembly = part_1.union(part_2)
cq.exporters.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2000.stl