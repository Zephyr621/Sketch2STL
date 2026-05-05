import cadquery as cq
# --- Part 1: Cube with Hole ---
cube_size = 0.5455 * 0.5455  # Sketch size scaled
hole_radius = 0.1308 * 0.5455  # Sketch radius scaled
extrude_depth = 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(cube_size, cube_size)
    .extrude(extrude_depth)
    .faces(">Z").workplane()
    .circle(hole_radius)
    .cutThruAll()
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
cq.
cq.
cq.
cq.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_721.stl