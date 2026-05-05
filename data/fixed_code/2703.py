import cadquery as cq
from cadquery.vis import show
# --- Part 1: Rectangular Plate with Rounded Corners ---
sketch_scale = 0.75
length = 0.75 * sketch_scale
width = 0.5 * sketch_scale
height = 0.025
corner_radius = 0.0125 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, corner_radius)
    .threePointArc((corner_radius, 0), (0.0031 * sketch_scale, 0.0031 * sketch_scale))
    .lineTo(length - corner_radius, 0)
    .threePointArc((length, corner_radius), (0.75 * sketch_scale, 0.0031 * sketch_scale))
    .lineTo(length, width - corner_radius)
    .threePointArc((length - corner_radius, width), (0.0031 * sketch_scale, width - corner_radius))
    .lineTo(corner_radius, width)
    .threePointArc((0, width - corner_radius), (0.0031 * sketch_scale, width - corner_radius))
    .close()
    .extrude(height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2703.stl