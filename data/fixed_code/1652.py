import cadquery as cq
# --- Part 1: Rectangular Plate ---
part_1_length = 0.5824 * 0.75  # Scaled length
part_1_width = 0.75 * 0.75   # Scaled width
part_1_height = 0.0397
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Part 2: Cylinder Cutout ---
part_2_radius = 0.0129 * 0.0273  # Scaled radius
part_2_depth = 0.0078
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_radius)
    .extrude(-part_2_depth)
)
# --- Coordinate System Transformations ---
# Part 1: Rotate and Translate
part_1 = part_1.rotate((0, 0, 0), (1, 0, 0), -90)
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
# Part 2: Rotate and Translate
part_2 = part_2.rotate((0, 0, 0), (1, 0, 0), -90)
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1652.stl