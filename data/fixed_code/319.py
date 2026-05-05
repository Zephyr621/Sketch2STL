import cadquery as cq
# --- Part 1: L-shaped Bracket ---
sketch_scale = 0.75
extrude_depth = 0.0312 * sketch_scale
# Scaled dimensions
width = 0.75 * sketch_scale
length = 0.7125 * sketch_scale
thickness = 0.0062 * sketch_scale
# Hole parameters (scaled)
hole1_center = (0.0206 * sketch_scale, 0.375 * sketch_scale)
hole2_center = (0.7266 * sketch_scale, 0.375 * sketch_scale)
hole3_center = (0.7266 * sketch_scale, 0.3728 * sketch_scale)
hole4_center = (0.7266 * sketch_scale, 0.6522 * sketch_scale)
# Create the base L-shape with rounded edges
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(width, 0)
    .lineTo(width, thickness)
    .lineTo(thickness, thickness)
    .lineTo(thickness, 0.6 * sketch_scale)
    .lineTo(0.0725 * sketch_scale, 0.6 * sketch_scale)
    .lineTo(0.0725 * sketch_scale, thickness)
    .lineTo(0, thickness)
    .close()
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_319.stl