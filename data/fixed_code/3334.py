import cadquery as cq
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_height = 0.0238
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(-part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0238, 0))
# --- Part 2: Cut Feature ---
sketch_scale = 0.675
cut_depth = 0.0313
cut_feature = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.0563 * sketch_scale, 0.0)
    .threePointArc((0.1687 * sketch_scale, 0.1687 * sketch_scale), (0.6836 * sketch_scale, 0.1725 * sketch_scale))
    .lineTo(0.3505 * sketch_scale, 0.1725 * sketch_scale)
    .threePointArc((0.2109 * sketch_scale, 0.1687 * sketch_scale), (0.0, 0.0))
    .close()
)
cut_feature = cut_feature.extrude
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_3334.stl