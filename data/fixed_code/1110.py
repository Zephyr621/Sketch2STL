import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder ---
part_1_length = 0.75 * 0.75  # Sketch length scaled
part_1_width = 0.3214 * 0.75  # Sketch width scaled
part_1_height = 0.2557
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(part_1_length, 0.0)
    .lineTo(part_1_length, part_1_width)
    .lineTo(0.0536 * 0.75, part_1_width)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.2557, 0))
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1110.stl