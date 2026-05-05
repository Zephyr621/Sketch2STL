import cadquery as cq
# --- Part 1: L-shaped CAD Model ---
sketch_scale = 0.75
extrude_depth = 0.3092 * sketch_scale
# Scaled dimensions
width_1 = 0.3092 * sketch_scale
width_2 = 0.1414 * sketch_scale
height_1 = 0.3092 * sketch_scale
height_2 = 0.2885 * sketch_scale
height_3 = 0.4286 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(width_1, 0)
    .lineTo(width_1, height_1)
    .lineTo(0, height_1)
    .close()
    .moveTo(width_2, 0)
    .lineTo(width_2, height_1)
    .lineTo(width_2, height_2)
    .lineTo(width_2, height_3)
    .lineTo(width_2, height_3)
    .lineTo(0, height_3)
    .close()
    .moveTo(width_2, height_3)
    .lineTo(width_2, height_3)
    .lineTo(width_2, height_2)
    .lineTo(width_2, height_2)
    .
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1319.stl