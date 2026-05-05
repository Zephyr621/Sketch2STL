import cadquery as cq
from cadquery import exporters
# --- Part 1: Base with Protrusion ---
base_width = 0.5357 * 0.75
base_height = 0.3587 * 0.75
protrusion_width = (0.4286 - 0.1829) * 0.75
protrusion_height = 0.3587 * 0.75
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(base_width, 0)
    .lineTo(base_width, base_height)
    .lineTo(0.5625 * 0.75, base_height)
    .lineTo(0.5625 * 0.75, 0.1829 * 0.75)
    .lineTo(0.1829 * 0.75, 0.1829 * 0.75)
    .lineTo(0.1829 * 0.75, base_height)
    .lineTo(0, base_height)
    .close()
    .extrude(base_height)
)
# --- Part 2: Cylindrical Protrusions ---
cylinder_radius = 0.0357 * 0.0714
cylinder_height = 0.3878
# Create the cylinders
cylinders = []
for i in range(6):
    angle = 2 * math.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_680.stl