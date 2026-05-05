import cadquery as cq
# --- Part 1: Cube with Rounded Edges ---
length = 0.75 * 0.75  # Scaled length
width = 0.4375 * 0.75  # Scaled width
height = 0.125
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(length, 0)
    .threePointArc((length/2, 0), (0.375 * 0.75, width))
    .lineTo(0, width)
    .close()
    .extrude(height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.125, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
cq.
cq.
cq.
cq.cq.exporters.export(assembly
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_790.stl