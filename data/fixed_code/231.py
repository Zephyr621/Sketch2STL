import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder ---
part_1_radius = 0.1385 * 0.75  # Sketch radius scaled
part_1_height = 0.2604
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.2604, 0))
# --- Part 2: Rectangular Cylinder ---
part_2_outer_radius = 0.1385 * 0.75  # Sketch radius scaled
part_2_inner_radius = 0.1171 * 0.75
part_2_height = 0.2604
part_2 = (
    cq.Workplane("XY")
    .moveTo(0.1385 * 0.75, 0.1385 * 0.75)
    .circle(part_2_outer_radius)
    .moveTo(0.1385 * 0.75, 0.6136 * 0.75)
    .circle(part_2_inner_radius)
    .extrude(-part_2_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part
# Export
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_231.stl