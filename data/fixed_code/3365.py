import cadquery as cq
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_height = 0.0209
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0209, 0))
# --- Part 2: Rod ---
outer_radius = 0.3529 * 0.7031  # Outer radius scaled
inner_radius = 0.3515 * 0.7031
part_2_height = 0.2945
part_2 = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .circle(inner_radius)
    .extrude(-part_2_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_3365.stl