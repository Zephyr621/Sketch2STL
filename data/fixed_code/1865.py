import cadquery as cq
# --- Part 1: Rectangular Plate ---
part_1_length = 0.6346 * 0.75  # Scaled length
part_1_width = 0.75 * 0.75  # Scaled width
part_1_height = 0.0192
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)  # Extrude in the opposite direction
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.0094))
# --- Part 2: Rectangular Frame ---
frame_length = 0.6346 * 0.6346  # Scaled length
frame_width = 0.75 * 0.6346  # Scaled width
frame_height = 0.0434
frame = (
    cq.Workplane("XY")
    .rect(frame_length, frame_width)
    .extrude(frame_height)
)
# --- Coordinate System Transformation for Frame ---
frame = frame.rotate((0, 0, 0), (0, 0, 1), -90)
frame = frame.translate((0, 0.0434, 0))
# --- Assembly
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1865.stl