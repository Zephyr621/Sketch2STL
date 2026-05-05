import cadquery as cq
from cadquery.vis import show
# --- Part 1: Rectangular Plate with Rounded Edges ---
length = 0.75 * 0.75  # Scaled length
width = 0.3871 * 0.75  # Scaled width
height = 0.0484
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(length, 0.0)
    .lineTo(length, width)
    .lineTo(0.0, width)
    .close()
    .extrude(height)
)
# Create the hole
hole_radius = 0.0246 * 0.75  # Scaled radius
part_1 = part_1.faces(">Z").workplane().circle(hole_radius).cutThruAll()
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0484, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# Export to
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2988.stl