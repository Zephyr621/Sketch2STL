import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Rectangular Base with Curved Top ---
part_1_length = 0.0674
part_1_width = 0.0545
part_1_height = 0.0365
sketch_scale_1 = 0.0674
scaled_length = part_1_length * sketch_scale_1
scaled_width = part_1_width * sketch_scale_1
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(scaled_length, 0)
    .lineTo(scaled_length, scaled_width)
    .threePointArc((0.0117 * sketch_scale_1, scaled_width/2), (scaled_length/2, scaled_width))
    .lineTo(0, scaled_width)
    .close()
    .extrude(part_1_height)
)
# --- Part 2: Cutout Feature ---
part_2_length = 0.0061
part_2_width = 0.051
part_2_height = 0.0234
sketch_scale_2 = 0.0061
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2668.stl