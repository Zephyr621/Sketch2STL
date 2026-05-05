import cadquery as cq
# --- Part 1: Rectangular Base ---
base_length = 0.75 * 0.75
base_width = 0.0495 * 0.75
base_height = 0.5357
part_1 = (
    cq.Workplane("XY")
    .rect(base_length, base_width)
    .extrude(base_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.5357, 0))
# --- Part 2: Triangular Cutout ---
cutout_length = 0.6429 * 0.6429
cutout_width = 0.0536 * 0.6429
cutout_height = 0.2143
part_2 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(cutout_length, 0)
    .lineTo(cutout_length, cutout_width)
    .lineTo(0, cutout_width)
    .close()
    .extrude(-cutout_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1175.stl