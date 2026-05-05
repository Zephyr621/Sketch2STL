import cadquery as cq
# --- Part 1: Cube with Cut Off ---
cube_size = 0.75 * 0.75  # Scaled size
cutout_x = 0.2188 * 0.75  # Scaled cutout x position
cutout_y = 0.1687 * 0.75  # Scaled cutout y position
extrude_depth = 0.75
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(cube_size, 0)
    .lineTo(cube_size, cube_size)
    .lineTo(0, cube_size)
    .close()
    .extrude(extrude_depth)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.cq.exporters.export(
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2585.stl