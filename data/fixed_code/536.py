import cadquery as cq
# --- Part 1: Rectangular Frame ---
length = 0.75 * 0.75  # Scaled length
width = 0.5357 * 0.75  # Scaled width
height = 0.2606
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0.0212, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# --- Export to STL ---
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# --- Final Result ---
result = assembly
cq.exporters
# 导出为STL文件
cq.exporters.export(result, "output_536.stl