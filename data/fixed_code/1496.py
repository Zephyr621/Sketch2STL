import cadquery as cq
# --- Part 1: Cylinder with Holes ---
sketch_scale = 0.75
outer_radius = 0.2109 * sketch_scale
inner_radius = 0.1065 * sketch_scale
hole1_center = (0.2156 * sketch_scale, 0.2194 * sketch_scale)
hole2_center = (0.5319 * sketch_scale, 0.2194 * sketch_scale)
hole3_center = (0.7113 * sketch_scale, 0.2194 * sketch_scale)
hole_radius = 0.0596 * sketch_scale
extrude_depth = 0.2031
part_1 = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .extrude(extrude_depth)
    .faces(">Z")
    .workplane()
    .pushPoints([hole1_center, hole2_center, hole3_center])
    .hole(2 * hole_radius)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.2031, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.cq.exporters.export(assembly,
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1496.stl