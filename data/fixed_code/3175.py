import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Cylinder ---
sketch_scale = 0.75
extrude_depth = 0.0051 * 2  # Total extrusion depth (both directions)
# Scaled dimensions
start_x1 = 0.0461 * sketch_scale
end_x1 = 0.6955 * sketch_scale
mid_arc1 = 0.7207 * sketch_scale
end_arc1 = 0.6895 * sketch_scale
mid_arc2 = 0.75 * sketch_scale
# Create the base cylinder
base_cylinder = (
    cq.Workplane("XY")
    .moveTo(start_x1, 0)
    .lineTo(end_x1, 0)
    .threePointArc((mid_arc1, mid_arc1), (end_x1, end_arc1))
    .lineTo(start_x1, end_arc1)
    .threePointArc((0, mid_arc2), (start_x1, 0))
    .close()
)
# Extrude the base cylinder
part_1 = base_cylinder.extrude(extrude_depth)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0
# Export
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_3175.stl