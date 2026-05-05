import cadquery as cq
# --- Parameters from JSON ---
length = 0.75 * 0.75  # Scaled length
width = 0.3472 * 0.75  # Scaled width
height = 0.2885
cutout_x1 = 0.0214 * 0.75
cutout_x2 = 0.7146 * 0.75
cutout_y = 0.0464 * 0.75
cutout_y2 = 0.0464 * 0.75
# --- Part 1: Rectangular Plate with Cutout ---
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
)
# --- Part 2: Cylinder (Cutout) ---
part_2_radius = 0.0879 * 0.1776
part_2_depth = 0.2885
part_2 = (
    cq.Workplane("XY")
    .moveTo(0.0879 * 0.1776, 0.0879 * 0.1776)
    .circle(part_2_radius)
    .extrude(-part_2_depth)
)
# --- Assembly: Cut Part 2 from Part 1 ---
assembly = part_1.cut(part_2.translate((0.1621, 0.0879, height)))
# --- Export to STL ---
cq.
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_920.stl