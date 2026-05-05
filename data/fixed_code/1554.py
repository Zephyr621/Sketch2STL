import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.0365
extrude_depth = 0.75
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0 * sketch_scale, 0.0039 * sketch_scale)
    .lineTo(0.0039 * sketch_scale, 0.0 * sketch_scale)
    .threePointArc((0.0157 * sketch_scale, 0.0157 * sketch_scale), (0.0039 * sketch_scale, 0.0033 * sketch_scale))
    .lineTo(0.0039 * sketch_scale, 0.0117 * sketch_scale)
    .threePointArc((0.0157 * sketch_scale, 0.0157 * sketch_scale), (0.0 * sketch_scale, 0.0033 * sketch_scale))
    .lineTo(0.0 * sketch_scale, 0.0039 * sketch_scale)
    .close()
    .extrude(extrude_depth)
)
# Create the hole
hole_radius = 0.0099 * sketch_scale
part_1 = part_1.faces(">Z").workplane().circle(hole_radius).cutThruAll()
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1554.stl