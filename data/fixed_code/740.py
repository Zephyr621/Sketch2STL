import cadquery as cq
# --- Part 1: Rectangular Box ---
part_1_length = 0.54545454545454545 * 0.54545  # Sketch length scaled
part_1_width = 0.1083 * 0.54545454545454545
part_1_height = 0.375
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
# --- Part 2: Rectangular Prism ---
part_2_length = 0.0542 * 0.0937  # Sketch length scaled
part_2_width = 0.0937 * 0.0937  # Sketch width scaled
part_2_height = 0.1125
part_2 = (
    cq.Workplane("XY")
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_740.stl