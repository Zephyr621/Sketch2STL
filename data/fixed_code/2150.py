import cadquery as cq
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.0025 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * sketch_scale, 0.0)
    .lineTo(0.75 * sketch_scale, 0.3772 * sketch_scale)
    .lineTo(0.0, 0.3772 * sketch_scale)
    .close()
    .extrude(extrude_depth)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0025 * sketch_scale, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.
cq.exp
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2150.stl