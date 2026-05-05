import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cube with Curved Top ---
sketch_scale = 0.7389
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0 * sketch_scale, 0.0246 * sketch_scale)
    .lineTo(0.2143 * sketch_scale, 0.0246 * sketch_scale)
    .threePointArc((0.3286 * sketch_scale, 0.0436 * sketch_scale), (0.3229 * sketch_scale, 0.0 * sketch_scale))
    .lineTo(0.6489 * sketch_scale, 0.0 * sketch_scale)
    .threePointArc((0.6136 * sketch_scale, 0.0848 * sketch_scale), (0.6489 * sketch_scale, 0.7389 * sketch_scale))
    .lineTo(0.0246 * sketch_scale, 0.7389 * sketch_scale)
    .threePointArc((0.0113 * sketch_scale, 0.6614 * sketch_scale), (0.0 * sketch_scale, 0.0246 * sketch_scale))
    .close()
    .extrude(0.5407 * sketch_scale)
)
# --- Assembly (if needed, based on the single part) ---
# In this case,
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1506.stl