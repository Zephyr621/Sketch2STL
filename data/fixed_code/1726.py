import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.1434 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.2311 * sketch_scale)
    .threePointArc((0.375 * sketch_scale, 0.0), (0.75 * sketch_scale, 0.2311 * sketch_scale))
    .lineTo(0.75 * sketch_scale, 0.4286 * sketch_scale)
    .threePointArc((0.375 * sketch_scale, 0.4688 * sketch_scale), (0.0, 0.4286 * sketch_scale))
    .lineTo(0.0, 0.2311 * sketch_scale)
    .close()
    .extrude(extrude_depth)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.1434 * sketch_scale, 0))
# --- Assembly ---
assembly = part_1
cq.cq.exporters.export(assembly
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1726.stl