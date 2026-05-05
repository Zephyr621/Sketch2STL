import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder ---
sketch_scale = 0.75
extrude_depth = 0.0313 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.3289 * sketch_scale)
    .lineTo(0.1875 * sketch_scale, 0.0)
    .lineTo(0.5625 * sketch_scale, 0.0)
    .lineTo(0.75 * sketch_scale, 0.3289 * sketch_scale)
    .lineTo(0.5625 * sketch_scale, 0.6495 * sketch_scale)
    .lineTo(0.1875 * sketch_scale, 0.6495 * sketch_scale)
    .lineTo(0.0, 0.3289 * sketch_scale)
    .close()
    .extrude(extrude_depth)
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_90.stl