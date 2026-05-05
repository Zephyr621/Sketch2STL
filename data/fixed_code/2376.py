import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.0536 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.1248 * sketch_scale, 0)
    .threePointArc((0.375 * sketch_scale, 0.0313 * sketch_scale), (0.6328 * sketch_scale, 0))
    .lineTo(0.75 * sketch_scale, 0)
    .threePointArc((0.7396 * sketch_scale, 0.1248 * sketch_scale), (0.6977 * sketch_scale, 0.2515 * sketch_scale))
    .lineTo(0.1248 * sketch_scale, 0.2515 * sketch_scale)
    .threePointArc((0.0, 0.1248 * sketch_scale), (0.1248 * sketch_scale, 0))
    .close()
    .extrude(extrude_depth)
)
# Create holes in part 1
hole_radius = 0.0476 * sketch_scale
part_1 = part_1.faces(">Z").workplane().pushPoints([
    (0.2393
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2376.stl