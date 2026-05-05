import cadquery as cq
from math import radians
# --- Part 1: Cylinder with Protrusion ---
sketch_scale = 0.0312
extrude_depth = 0.75
# Define the points for the sketch (scaled)
p1 = (0.0039 * sketch_scale, 0.0146 * sketch_scale)
p2 = (0.0124 * sketch_scale, 0.0146 * sketch_scale)
p3 = (0.0124 * sketch_scale, 0.0284 * sketch_scale)
p4 = (0.0039 * sketch_scale, 0.0284 * sketch_scale)
# Create the sketch using arcs and lines
part_1 = (
    cq.Workplane("XY")
    .moveTo(p1[0], p1[1])
    .threePointArc((0.0045 * sketch_scale, 0.0045 * sketch_scale), p2)
    .lineTo(p3[0], p3[1])
    .threePointArc((0.0045 * sketch_scale, 0.0045 * sketch_scale), p4)
    .close()
    .extrude(extrude_depth)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2146.stl