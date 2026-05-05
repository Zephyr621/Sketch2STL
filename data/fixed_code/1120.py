import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder ---
sketch_scale = 0.75
extrude_depth = 0.0804 * 2  # Total extrusion depth (towards + opposite normal)
# Define circle centers and radius for the sketch
circle1_center = (0.1117 * sketch_scale, 0.1667 * sketch_scale)
circle2_center = (0.6198 * sketch_scale, 0.1667 * sketch_scale)
circle3_center = (0.75 * sketch_scale, 0.1667 * sketch_scale)
circle4_center = (0.5981 * sketch_scale, 0.1667 * sketch_scale)
# Create the base shape using arcs
part_1 = (
    cq.Workplane("XY")
    .moveTo(circle1_center[0], circle1_center[1])
    .threePointArc(circle1_center, circle2_center)
    .lineTo(circle2_center[0], circle2_center[1])
    .threePointArc(circle2_center, circle3_center)
    .lineTo(circle4_center[0], circle4_center[1])
    .close()
    .extrude(extrude_depth)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1120.stl