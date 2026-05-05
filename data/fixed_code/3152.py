import cadquery as cq
# --- Part 1: Cube ---
part_1_size = 0.75 * 0.75  # Sketch size scaled
part_1_extrude = 0.75
part_1 = cq.Workplane("XY").box(part_1_size, part_1_size, part_1_extrude)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
cq.
cq.
cq.
cq.
cq.
cq.exporters
# 导出为STL文件
cq.exporters.export(result, "output_3152.stl