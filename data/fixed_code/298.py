import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Flat Plate ---
sketch_scale = 0.75
extrude_depth = 0.0067 * sketch_scale
# Scaled coordinates
p1 = (0.1749 * sketch_scale, 0.0)
p2 = (0.6207 * sketch_scale, 0.0)
p3 = (0.7498 * sketch_scale, 0.4554 * sketch_scale)
p4 = (0.75 * sketch_scale, 0.5324 * sketch_scale)
p5 = (0.5557 * sketch_scale, 0.5324 * sketch_scale)
p6 = (0.3384 * sketch_scale, 0.5324 * sketch_scale)
p7 = (0.1622 * sketch_scale, 0.5068 * sketch_scale)
p8 = (0.1749 * sketch_scale, 0.5068 * sketch_scale)
p9 = (0.1749 * sketch_scale, 0.5312 * sketch_scale)
p10 = (0.0824 * sketch_scale, 0.5312 * sketch_scale)
p11 = (0.0403 * sketch_scale, 0.5312 * sketch_scale)
p12 = (0.0, 0.4554 * sketch_scale)
part_1 = (
    cq.Workplane("XY")
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_298.stl