import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cube with Rounded Edges ---
sketch_scale = 0.75
length = 0.75 * sketch_scale
width = 0.5714 * sketch_scale
height = 0.0268
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0107 * sketch_scale)
    .lineTo(0.0107 * sketch_scale, 0.0)
    .threePointArc((0.375 * sketch_scale, 0.3029 * sketch_scale), (0.7222 * sketch_scale, 0.0))
    .lineTo(0.75 * sketch_scale, 0.0107 * sketch_scale)
    .lineTo(0.75 * sketch_scale, 0.5714 * sketch_scale)
    .lineTo(0.0, 0.5714 * sketch_scale)
    .lineTo(0.0, 0.0107 * sketch_scale)
    .close()
    .extrude(height)
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_698.stl