import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Curved Shape ---
sketch_scale = 0.75
part_1_radius = 0.375 * sketch_scale  # Sketch radius scaled
part_1_height = 0.0033
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.125 * sketch_scale, 0)
    .lineTo(0.625 * sketch_scale, 0)
    .threePointArc((0.75 * sketch_scale, 0.25 * sketch_scale), (0.625 * sketch_scale, 0.5 * sketch_scale))
    .lineTo(0.125 * sketch_scale, 0.5 * sketch_scale)
    .threePointArc((0, 0.25 * sketch_scale), (0.125 * sketch_scale, 0))
    .close()
    .extrude(-part_1_height)
)
# Create the hole
hole_radius = 0.0302 * sketch_scale
part_1 = part_1.faces(">Z").workplane().circle(hole_radius).cutThruAll()
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Assembly (if needed, based
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2817.stl