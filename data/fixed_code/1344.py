import cadquery as cq
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_height = 0.0208 + 0.0208
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0938, 0))
# --- Part 2: Cut Feature ---
part_2_width = 0.0417 * 0.1419  # Sketch width scaled
part_2_depth = 0.1419 * 0.1419  # Sketch depth scaled
part_2_height = 0.1829
cut_feature = (
    cq.Workplane("XY")
    .moveTo(0, 0.0417 * 0.1419)
    .threePointArc((0.0054 * 0.1419, 0), (0.0417 * 0.1419, 0.0417 * 0.1419))
    .lineTo(0, 0.0417 * 0.1419)
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_1344.stl