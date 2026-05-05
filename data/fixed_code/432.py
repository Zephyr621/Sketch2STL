import cadquery as cq
# --- Part 1: Cube with Cutout ---
length = 0.75 * 0.75  # Scaled length
width = 0.5 * 0.75  # Scaled width
height = 0.25
cutout_x = 0.125 * 0.75  # Scaled cutout x
cutout_y = 0.125 * 0.75  # Scaled cutout y
cutout_size = (0.375 - 0.0625) * 0.75  # Scaled cutout size
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
    .faces(">Z").workplane()
    .rect(cutout_size, cutout_size)
    .cutThruAll()
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.25, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_432.stl