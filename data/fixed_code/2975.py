import cadquery as cq
# --- Part 1: Rectangular Plate ---
plate_length = 0.45 * 0.45  # Scaled length
plate_width = 0.5 * 0.45  # Scaled width
plate_height = 0.06
part_1 = (
    cq.Workplane("XY")
    .rect(plate_length, plate_width)
    .extrude(plate_height)
)
# --- Part 2: Cylindrical Protrusions ---
cylinder_radius = 0.15 * 0.75
cylinder_depth = 0.06
# Define cylinder positions relative to the plate's origin
cylinder_positions = [
    (-0.15 * 0.75, -0.15 * 0.75),
    (0.15 * 0.75, 0.3 * 0.75),
    (0.6 * 0.75, -0.15 * 0.75)
]
# Create cylinders by cutting cylinders
for x, y in cylinder_positions:
    cylinder = cq.Workplane("XY").circle(cylinder_radius).extrude(-cylinder_depth)
    part_1 = part_1.cut(cylinder)
# --- Assembly ---
assembly = part_1
# --- Export to STL ---
cq.
# --- Export to STL
# 定义结果变量
result = cylinder
# 导出为STL文件
cq.exporters.export(result, "output_2975.stl