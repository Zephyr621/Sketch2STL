import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder ---
part_1_length = 0.75 * 0.75  # Sketch length scaled
part_1_width = 0.6387 * 0.75  # Sketch width scaled
part_1_height = 0.1224
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(part_1_length, 0.0)
    .threePointArc((part_1_length + 0.0238 * 0.75, part_1_width/2), (0.0, 0.0))
    .close()
    .extrude(part_1_height)
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
# Export to STL
cq.
cq.
cq
# 导出为STL文件
cq.exporters.export(result, "output_583.stl