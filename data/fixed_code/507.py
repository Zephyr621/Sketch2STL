import cadquery as cq
# --- Part 1: L-shaped CAD Model ---
sketch_scale = 0.75
extrude_depth = 0.0536 * sketch_scale
# Scaled dimensions
width_small = 0.7454 * sketch_scale
width_large = 0.6593 * sketch_scale
height = 0.0451 * sketch_scale
# Create the base shape with rounded corners
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(width_large, 0)
    .lineTo(width_large, height)
    .lineTo(0.0352 * sketch_scale, height)
    .lineTo(0.0352 * sketch_scale, 0.6986 * sketch_scale)
    .lineTo(0, 0.6986 * sketch_scale)
    .close()
    .moveTo(0.0179 * sketch_scale, 0.0352 * sketch_scale)
    .lineTo(0.7454 * sketch_scale, 0.0352 * sketch_scale)
    .lineTo(0.7454 * sketch_scale, 0.6742 * sketch_scale)
    .lineTo(0.7454 * sketch_scale, 0.6696 * sketch_scale)
    .lineTo(0.7454 * sketch_scale, 0.66
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_507.stl