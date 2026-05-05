import cadquery as cq
# --- Part 1: Rectangular Object ---
length = 0.75 * 0.75  # Scaled length
width = 0.5 * 0.75  # Scaled width
height = 0.2478
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.2478, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# --- Export to STL ---
cq.
# Export to STL
cq.
# --- Final Result ---
result = part_1
cq.
cq.
cq.cq.exporters.export(result
# 导出为STL文件
cq.exporters.export(result, "output_1051.stl