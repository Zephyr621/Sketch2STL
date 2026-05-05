import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder with Hole ---
sketch_scale = 0.75
extrude_depth = 0.2247
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0818 * sketch_scale, 0.3526 * sketch_scale)
    .threePointArc((0.375 * sketch_scale, 0.3248 * sketch_scale), (0.6631 * sketch_scale, 0.0))
    .lineTo(0.6429 * sketch_scale, 0.0)
    .threePointArc((0.75 * sketch_scale, 0.3382 * sketch_scale), (0.6429 * sketch_scale, 0.3526 * sketch_scale))
    .close()
    .extrude(extrude_depth)
)
# Add holes
hole_radius = 0.0421 * sketch_scale
part_1 = part_1.faces(">Z").workplane().pushPoints([(0.0818 * sketch_scale - (0.75 * sketch_scale)/2, 0.3248 * sketch_scale - (0.6328 * sketch_scale)/2)]).hole(hole_radius * 2)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3325.stl