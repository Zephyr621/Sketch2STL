import cadquery as cq
from cadquery.vis import show
# --- Part 1: Teardrop ---
sketch_scale = 0.75
extrude_depth = 0.2143 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0 * sketch_scale, 0.4286 * sketch_scale)
    .threePointArc((0.375 * sketch_scale, 0.2214 * sketch_scale), (0.7161 * sketch_scale, 0.4286 * sketch_scale))
    .threePointArc((0.75 * sketch_scale, 0.2242 * sketch_scale), (0.7161 * sketch_scale, 0.4479 * sketch_scale))
    .threePointArc((0.375 * sketch_scale, 0.2242 * sketch_scale), (0.0 * sketch_scale, 0.4479 * sketch_scale))
    .close()
    .extrude(extrude_depth)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.2143))
# --- Assembly ---
assembly = part_1
cq.
# Export to STL
cq.exporters
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1916.stl