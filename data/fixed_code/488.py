import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Octagonal Block with Curved Edges ---
sketch_scale = 0.75
extrude_depth = 0.0786 * 2  # Total depth (both directions)
# Scaled coordinates for the octagon
points = [
    (0.0 * sketch_scale, 0.3248 * sketch_scale),
    (0.1877 * sketch_scale, 0.0 * sketch_scale),
    (0.5625 * sketch_scale, 0.0 * sketch_scale),
    (0.75 * sketch_scale, 0.3248 * sketch_scale),
    (0.5625 * sketch_scale, 0.6495 * sketch_scale),
    (0.1877 * sketch_scale, 0.6495 * sketch_scale),
    (0.0 * sketch_scale, 0.3248 * sketch_scale)
]
# Create the octagon using the points
part_1 = (
    cq.Workplane("XY")
    .polyline(points)
    .close()
    .extrude(extrude_depth)
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_488.stl