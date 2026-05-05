import cadquery as cq
# --- Part 1: Cube with Cutout ---
length = 0.75 * 0.75  # Scaled length
width = 0.3705 * 0.75  # Scaled width
height = 0.7462
hole_radius = 0.0369 * 0.75  # Scaled radius
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
    .faces(">Z")
    .workplane()
    .pushPoints([
        (0.1293 * 0.75 - length/2 + hole_radius, 0),
        (0.2438 * 0.75 - length/2 + hole_radius, 0),
        (0.6094 * 0.75 - length/2 + hole_radius, 0)
    ])
    .hole(2 * hole_radius)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.7462, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.cq.exporters.export(
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_57.stl