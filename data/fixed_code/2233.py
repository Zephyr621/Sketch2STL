import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder with Hollow Center ---
sketch_scale = 0.75
extrude_depth = 0.1691 * 2  # Total extrusion depth (towards + opposite normal)
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.1503 * sketch_scale, 0.0 * sketch_scale)
    .threePointArc((0.375 * sketch_scale, 0.1267 * sketch_scale), (0.6328 * sketch_scale, 0.0 * sketch_scale))
    .lineTo(0.75 * sketch_scale, 0.0 * sketch_scale)
    .threePointArc((0.5625 * sketch_scale, 0.1862 * sketch_scale), (0.6328 * sketch_scale, 0.3701 * sketch_scale))
    .lineTo(0.1503 * sketch_scale, 0.3701 * sketch_scale)
    .threePointArc((0.0 * sketch_scale, 0.1862 * sketch_scale), (0.1503 * sketch_scale, 0.0 * sketch_scale))
    .close()
    .extrude(extrude_depth)
)
# Create the hole
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2233.stl