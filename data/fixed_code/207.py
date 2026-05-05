import cadquery as cq
# --- Part 1: Rectangular Block ---
length = 0.25 * 0.25  # Scaled length
width = 0.0833 * 0.25  # Scaled width
height = 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(-height)  # Extrude in the opposite direction
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Final Result ---
result = assembly
cq.
cq.
# 导出为STL文件
cq.exporters.export(result, "output_207.stl