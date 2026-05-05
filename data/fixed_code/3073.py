import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder ---
part_1_radius = 0.0483 * 0.0938  # Sketch radius scaled
part_1_height = 0.6818
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(-part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.0483, 0.0483, 0.0854))
# --- Part 2: Rectangular Protrusion ---
part_2_width = 0.0938 * 0.75  # Sketch width scaled
part_2_length = 0.75 * 0.75  # Sketch length scaled
part_2_height = 0.0417
part_2 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(part_2_length, 0.0)
    .lineTo(part_2_length, part_2_width)
    .lineTo(0.0, part_2_width)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(part_2_height)
)
# --- Assembly ---
assembly
# Export
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_3073.stl