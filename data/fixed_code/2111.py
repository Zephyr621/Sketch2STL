import cadquery as cq
# --- Part 1: Cube with Rounded Edges ---
length = 0.0469 * 0.0469  # Scaled length
width = 0.0262 * 0.0469  # Scaled width
height = 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(-height)  # Extrude in the opposite direction
)
# Apply rotation: Euler angles (0, 0, -90 degrees) => Rotate around Z
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
# Apply translation: (0, 0, 0) - No translation needed
# --- Assembly ---
result = part_1
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL
# 导出为STL文件
cq.exporters.export(result, "output_2111.stl