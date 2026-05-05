import cadquery as cq
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_height = 0.0195
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(-part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Part 2: Ring ---
outer_radius = 0.3656 * 0.7368
inner_radius = 0.3548 * 0.7368
ring_height = 0.0769
part_2 = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .circle(inner_radius)
    .extrude(ring_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.0198, 0, 0.0198))
# --- Assembly ---
assembly = part_1.union(part_2)
# --- Export to STL ---
exporters
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_1155.stl