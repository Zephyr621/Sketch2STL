import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder ---
part_1_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_height = 0.2019
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.2019, 0))
# --- Part 2: Rods ---
outer_radius = 0.3079 * 0.75
inner_radius = 0.3107 * 0.75
part_2_height = 0.1082
part_2 = (
    cq.Workplane("XY")
    .moveTo(0, outer_radius)
    .threePointArc((outer_radius, 0), (0.1536 * 0.75, 0.1536 * 0.75))
    .lineTo(0, outer_radius)
    .close()
    .moveTo(0.4363 * 0.75, 0)
    .threePointArc((outer_radius, 0.2062 * 0.75), (0.5644 * 0.75, 0))
    .lineTo(0.75 * 0.75, 0)
    .lineTo(0.75 * 0.75, 0.5941 * 0.75)
# Export
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_2599.stl