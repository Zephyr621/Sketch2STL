import cadquery as cq
# --- Part 1: Rectangular Block ---
part_1_length = 0.4618 * 0.75  # Scaled length
part_1_width = 0.75 * 0.75   # Scaled width
part_1_height = 0.3024
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)  # Extrude in the opposite direction for a cut
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.1562))
# --- Part 2: Rentagon ---
part_2_scale = 0.7222
part_2_depth = 0.2944
part_2 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.3789 * part_2_scale)
    .lineTo(0.0021 * part_2_scale, 0.0)
    .lineTo(0.3581 * part_2_scale, 0.4554 * part_2_scale)
    .lineTo(0.3788 * part_2_scale, 0.7222 * part_2_scale)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3286.stl