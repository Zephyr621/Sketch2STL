import cadquery as cq
# --- Part 1: Rectangular Bar ---
part_1_width = 0.0191 * 0.0296  # Sketch width scaled
part_1_height = 0.0296 * 0.0296 # Sketch height scaled
part_1_depth = 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_width, part_1_height)
    .extrude(-part_1_depth)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (1, 0, 0), -90)
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
cq.
# 导出为STL文件
cq.exporters.export(result, "output_183.stl