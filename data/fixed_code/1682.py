import cadquery as cq
# --- Part 1: Cube ---
part_1_size = 0.75 * 0.75  # Scaled size
part_1_height = 0.75
part_1 = cq.Workplane("XY").box(part_1_size, part_1_size, part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2: Cutout ---
part_2_x_offset = 0.6402
part_2_y_offset = 0.6256
part_2_z_offset = 0.0625
cutout_points = [
    (0.0, 0.3214),
    (0.4644, 0.0),
    (0.4644, 0.3214),
    (0.0, 0.3214),
]
cutout_2_points = [(x * 0.65, y * 0.65) for x, y in cutout_points]
cutout_3_points = [(x * 0.65, y * 0.65) for x, y in cutout_3_points]
cutout_4_points = [
    (0.0047, 0.0),
    (
# Export
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_1682.stl