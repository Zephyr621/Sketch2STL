import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Rectangular Plate ---
sketch_scale = 0.75
extrude_depth = 0.0112 * 2  # Total extrusion depth (towards + opposite normal)
# Define the points for the sketch
points = [
    (0.0037 * sketch_scale, 0.0037 * sketch_scale),
    (0.0037 * sketch_scale, 0.0345 * sketch_scale),
    (0.0037 * sketch_scale, 0.1172 * sketch_scale),
    (0.7347 * sketch_scale, 0.1172 * sketch_scale),
    (0.7347 * sketch_scale, 0.1405 * sketch_scale),
    (0.7347 * sketch_scale, 0.1369 * sketch_scale),
    (0.7347 * sketch_scale, 0.1369 * sketch_scale),
    (0.7347 * sketch_scale, 0.1172 * sketch_scale),
    (0.7347 * sketch_scale, 0.0785 * sketch_scale),
    (0.7347 * sketch_scale, 0.0785 * sketch_scale),
    (0.7347 * sketch_scale, 0.0492 *
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3500.stl