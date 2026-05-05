import cadquery as cq
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.3571 * 0.7166  # Sketch radius scaled
part_1_height = 0.6201
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.0205, 0.0205, 0))
# --- Part 2: Flange ---
part_2_outer_radius = 0.2143 * 0.4146  # Outer radius scaled
part_2_inner_radius = 0.2914 * 0.4146
part_2_height = 0.3281
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_outer_radius)
    .circle(part_2_inner_radius)
    .extrude(-part_2_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), 180)
part_2 = part_2.translate((0.0176, 0.75, 0))
# --- Assembly ---
assembly = part_1.union(part_2)
# --- Export to STL ---
cq.exporters.export(assembly,
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_107.stl