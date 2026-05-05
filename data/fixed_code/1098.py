import cadquery as cq
# --- Part 1: Cube ---
length = 0.75 * 0.75  # Scaled length
width = 0.625 * 0.75  # Scaled width
height = 0.5
part_1 = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Part 2: Cutout ---
cutout_x = 0.25 * 0.25  # Scaled cutout x
cutout_y = 0.125 * 0.25  # Scaled cutout y
cutout_depth = 0.25
cutout = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(cutout_x, 0)
    .lineTo(cutout_x, cutout_y)
    .lineTo(0, cutout_y)
    .close()
    .extrude(-cutout_depth)
)
# --- Coordinate System Transformation for Part 2 ---
cutout = cutout.rotate((0, 0, 0), (0, 0, 1), -90)
cutout = cutout.translate((0.25, 0, 0))
# --- Assembly: Cut Part 2 from Part 1 ---
result = part_1.cut(cutout)
# --- Export to STL ---
cq.
#
# 导出为STL文件
cq.exporters.export(result, "output_1098.stl