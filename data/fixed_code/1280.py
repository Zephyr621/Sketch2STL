import cadquery as cq
from cadquery.vis import show
# --- Part 1: Double Cylinder with Cutout ---
sketch_scale = 0.75
extrude_depth = 0.0409 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0193 * sketch_scale)
    .lineTo(0.0193 * sketch_scale, 0.0)
    .lineTo(0.7493 * sketch_scale, 0.0)
    .threePointArc((0.7311 * sketch_scale, 0.0747 * sketch_scale), (0.7232 * sketch_scale, 0.1955 * sketch_scale))
    .lineTo(0.75 * sketch_scale, 0.1955 * sketch_scale)
    .lineTo(0.75 * sketch_scale, 0.0391 * sketch_scale)
    .lineTo(0.0, 0.0391 * sketch_scale)
    .lineTo(0.0, 0.0193 * sketch_scale)
    .close()
    .extrude(extrude_depth)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1280.stl