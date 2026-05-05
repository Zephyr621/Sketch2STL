import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cube ---
sketch_scale = 0.75
length = 0.75 * sketch_scale
width = 0.5357 * sketch_scale
height = 0.0068
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .threePointArc((0.375 * sketch_scale, 0.2536 * sketch_scale), (0.75 * sketch_scale, 0.0))
    .lineTo(0.75 * sketch_scale, 0.1476 * sketch_scale)
    .lineTo(0.5417 * sketch_scale, 0.1476 * sketch_scale)
    .lineTo(0.5417 * sketch_scale, 0.5357 * sketch_scale)
    .threePointArc((0.375 * sketch_scale, 0.5357 * sketch_scale), (0.0, 0.5357 * sketch_scale))
    .lineTo(0.0, 0.0)
    .close()
    .extrude(height)
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1837.stl