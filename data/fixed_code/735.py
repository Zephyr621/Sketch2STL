import cadquery as cq
# --- Part 1: Cube with Rounded Edges and Corners ---
length = 0.75 * 0.75  # Scaled length
width = 0.75 * 0.75  # Scaled width
height = 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
)
# Apply rotation: Euler angles (0, 0, -90 degrees) => Rotate around Z
part_1 = part_1.rotate((0, 0, 0), (1, 0, 0), -90)
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
# Apply translation: (0, 0, 0) - No translation needed
# --- Assembly ---
result = part_1
# Export to STL
cq.
# --- Export to STL ---
cq.
# Export to STL
cq.
# --- Final Result ---
result = part_1
cq.
cq.exp
# 导出为STL文件
cq.exporters.export(result, "output_735.stl