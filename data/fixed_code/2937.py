import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.1299)
    .threePointArc((0.4837, 0.1299), (0.0, 0.1299))
    .close()
    .extrude(0.0068)
)
# Add holes
hole_radius = 0.0058 * 0.75
hole_centers = [
    (0.0602 * 0.75 - 0.0602 * 0.75, 0.0602 * 0.75 - 0.0602 * 0.75),
    (0.0602 * 0.75 - 0.0602 * 0.75, 0.2438 * 0.75 - 0.0602 * 0.75),
    (0.6802 * 0.75 - 0.0602 * 0.75, 0.0602 * 0.75 - 0.0602 * 0.75)
]
for center_x, center_y in hole_centers:
    part_1 = part_1.faces(">Z").workplane().pushPoints([(center_
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2937.stl