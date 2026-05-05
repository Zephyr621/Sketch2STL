import cadquery as cq
# --- Part 1: Rectangular Box ---
part_1_length = 0.5114 * 0.5114  # Sketch length scaled
part_1_width = 0.2393 * 0.5114  # Sketch width scaled
part_1_height = 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)  # Extrude in the opposite direction
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
cq.
cq.
cq.
# 导出为STL文件
cq.exporters.export(result, "output_929.stl