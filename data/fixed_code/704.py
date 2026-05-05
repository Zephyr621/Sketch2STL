import cadquery as cq
# --- Part 1: Cube with Circular Hole ---
cube_size = 0.75 * 0.75  # Scaled cube size
hole_radius = 0.125 * 0.75  # Scaled hole radius
extrude_depth = 0.5
part_1 = (
    cq.Workplane("XY")
    .rect(cube_size, cube_size)
    .extrude(extrude_depth)
    .faces(">Z")
    .workplane()
    .circle(hole_radius)
    .cutThruAll()
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.5, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.exporters.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_704.stl