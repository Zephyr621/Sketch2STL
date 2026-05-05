import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.0015 * 2  # Total extrusion depth (towards + opposite normal)
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.1611 * sketch_scale)
    .lineTo(0.3241 * sketch_scale, 0.0)
    .lineTo(0.7165 * sketch_scale, 0.1611 * sketch_scale)
    .threePointArc((0.747 * sketch_scale, 0.1689 * sketch_scale), (0.3241 * sketch_scale, 0.3311 * sketch_scale))
    .lineTo(0.0, 0.3333 * sketch_scale)
    .close()
    .moveTo(0.0119 * sketch_scale, 0.1611 * sketch_scale)
    .circle(0.0118 * sketch_scale)
    .extrude(extrude_depth)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0015, 0))
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1440.stl