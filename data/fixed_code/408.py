import cadquery as cq
from cadquery.vis import show
# --- Part 1: Rectangular Plate ---
length = 0.75 * 0.75  # Scaled length
width = 0.4831 * 0.75  # Scaled width
height = 0.0156
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(-height)  # Extrude in the opposite direction
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.0156))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# --- Final Result ---
result = assembly
cq.
# Export to STL
cq.
cq.
cq.
cq.
cq.
cq.cq.exporters.export(result,
# 导出为STL文件
cq.exporters.export(result, "output_408.stl