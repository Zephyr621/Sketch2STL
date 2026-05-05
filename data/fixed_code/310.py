import cadquery as cq
from cadquery.vis import show
# --- Part 1: Curved Rectangular Block with Holes ---
sketch_scale = 0.75
length = 0.75 * sketch_scale
width = 0.375 * sketch_scale
height = 0.2812
hole1_center = (0.1875 * sketch_scale, 0.0938 * sketch_scale)
hole1_radius = 0.0188 * sketch_scale
hole2_center = (0.5625 * sketch_scale, 0.0938 * sketch_scale)
hole2_radius = 0.0188 * sketch_scale
extrude_depth = 0.2813
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(length, 0)
    .threePointArc((length + hole1_center[0], 0), (length, width))
    .lineTo(0, width)
    .close()
    .extrude(extrude_depth)
)
part_1 = part_1.faces(">Z").workplane().pushPoints([hole1_center]).hole(2 * hole1_radius)
part_1 = part_1.faces("<Z").workplane().pushPoints([hole2_center]).hole(2 * hole2_radius)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.2812))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_310.stl