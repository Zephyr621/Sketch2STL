import cadquery as cq
from cadquery.vis import show
# --- Part 1: Triangle Prism ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.3 * 0.75, 0.0)
    .lineTo(0.3 * 0.75, 0.3 * 0.75)
    .threePointArc((0.225 * 0.75, 0.45 * 0.75), (0.375 * 0.75, 0.6 * 0.75))
    .lineTo(0.225 * 0.75, 0.6 * 0.75)
    .threePointArc((0.225 * 0.75, 0.45 * 0.75), (0.0, 0.3 * 0.75))
    .close()
    .extrude(0.15)
)
# Add holes to part 1
hole_radius = 0.075 * 0.75
part_1 = part_1.faces(">Z").workplane().pushPoints([(0.3 * 0.75 - 0.3 * 0.75/2, 0.15 * 0.75 - 0.3 * 0.75/2)]).hole(hole_radius * 2)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_664.stl