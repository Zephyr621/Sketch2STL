import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cube with Rounded Edges ---
sketch_scale = 0.75
extrude_depth = 0.2537
# Scaled dimensions
width = 0.75 * sketch_scale
length = 0.75 * sketch_scale
height = extrude_depth
# Create the base rectangular prism
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(length, 0)
    .lineTo(length, width)
    .lineTo(0, width)
    .close()
    .extrude(height)
)
# Apply rotation
part_1 = part_1.rotate((0, 0, 0), (1, 0, 0), -90)
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
# Apply translation
part_1 = part_1.translate((0.2537, 0, 0))
# Export to STL
cq.
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_452.stl