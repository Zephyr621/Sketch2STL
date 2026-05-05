import cadquery as cq
from cadquery.vis import show
# --- Part 1: Rectangular Block with Holes ---
length = 0.4209 * 0.4209  # Scaled length
width = 0.2344 * 0.4209   # Scaled width
height = 0.7031
hole_radius = 0.0525 * 0.4209  # Scaled radius
hole_center1 = (0.1136 * 0.4209 - length/2, 0.0937 * 0.4209 - width/2)  # Scaled and centered
hole_center2 = (0.2218 * 0.4209 - length/2, 0.0937 * 0.4209 - width/2)  # Scaled and centered
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
    .faces(">Z").workplane()
    .pushPoints([hole_center1, hole_center2])
    .hole(2 * hole_radius)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (1, 0, 0), -90)
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2948.stl