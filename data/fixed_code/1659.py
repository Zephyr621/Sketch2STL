import cadquery as cq
# --- Part 1: Cylinder ---
part_1_radius = 0.0179 * 0.0208  # Sketch radius scaled
part_1_height = 0.0048
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(-part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.0125))
# --- Part 2: Cut ---
part_2_scale = 0.0417
part_2 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.0076 * part_2_scale, 0.0)
    .lineTo(0.0076 * part_2_scale, 0.0417 * part_2_scale)
    .lineTo(0.0, 0.0417 * part_2_scale)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(-0.0124)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (1, 0
# Export
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_1659.stl