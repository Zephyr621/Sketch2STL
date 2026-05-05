import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder ---
part_1_radius = 0.0843 * 0.1786  # Sketch radius scaled
part_1_height = 0.75
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(-part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Part 2: Ring ---
outer_radius = 0.0843 * 0.1686
inner_radius = 0.0469 * 0.1686
ring_height = 0.5
part_2 = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .circle(inner_radius)
    .extrude(ring_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.0785, 0, 0.0785))
# --- Assembly ---
assembly = part_1.union(part_2)
cq.exporters
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_3001.stl