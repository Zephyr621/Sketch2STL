import cadquery as cq
from cadquery.vis import show
# --- Part 1: Triangular Prism ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.375 * 0.75, 0.75 * 0.75)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.375 * 0.75, 0.75 * 0.75)
    .close()
    .extrude(0.0089)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0089, 0))
# --- Part 2: Cylinder ---
part_2_radius = 0.375 * 0.75  # Sketch radius scaled
part_2_height = 0.0089
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(-part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0, 0, 0.0089))
# --- Assembly ---
assembly = part_1.union(part_2)
cq.
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_916.stl