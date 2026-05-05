import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder with Curved Top ---
sketch_scale = 0.75
extrude_depth = 0.375
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0625 * sketch_scale)
    .threePointArc((0.1353 * sketch_scale, 0.0), (0.7031 * sketch_scale, 0.0625 * sketch_scale))
    .lineTo(0.75 * sketch_scale, 0.0625 * sketch_scale)
    .lineTo(0.75 * sketch_scale, 0.1875 * sketch_scale)
    .lineTo(0.6 * sketch_scale, 0.1875 * sketch_scale)
    .threePointArc((0.375 * sketch_scale, 0.0938 * sketch_scale), (0.2188 * sketch_scale, 0.1875 * sketch_scale))
    .lineTo(0.0625 * sketch_scale, 0.1875 * sketch_scale)
    .lineTo(0.0625 * sketch_scale, 0.0625 * sketch_scale)
    .close()
    .extrude(extrude_depth)
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_524.stl