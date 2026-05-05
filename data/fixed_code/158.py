import cadquery as cq
# --- Part 1: Rectangular Plate with Holes ---
sketch_scale = 0.75
length = 0.75 * sketch_scale
width = 0.1324 * sketch_scale
height = 0.0104
hole_radius = 0.0395 * sketch_scale
hole_centers = [
    (0.0662 * sketch_scale, 0.0395 * sketch_scale),
    (0.0662 * sketch_scale, 0.1227 * sketch_scale),
    (0.5455 * sketch_scale, 0.0395 * sketch_scale)
]
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(0.7222 * sketch_scale, 0)
    .threePointArc((0.75 * sketch_scale, 0.0691 * sketch_scale), (0.75 * sketch_scale, 0.1227 * sketch_scale))
    .lineTo(0.7419 * sketch_scale, 0.1227 * sketch_scale)
    .threePointArc((0.6872 * sketch_scale, 0.0691 * sketch_scale), (0.7419 * sketch_scale, 0.1227 * sketch_scale))
    .lineTo(0.75 * sketch_scale,
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_158.stl