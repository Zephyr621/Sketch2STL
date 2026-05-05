import cadquery as cq
from cadquery.vis import show
# --- Part 1: Triangle Prism ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.0, 0.3571 * 0.75)
    .close()
    .extrude(0.0536)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.2303))
# --- Assembly ---
assembly = part_1
cq.
# --- Export to STL ---
cq.
# --- Final Result ---
result = assembly
cq.
cq.
cq.
cq.
# 导出为STL文件
cq.exporters.export(result, "output_1278.stl