import cadquery as cq
# --- Part 1: Cube ---
part_1_size = 0.75 * 0.75  # Sketch size scaled
part_1_height = 0.75
part_1 = cq.Workplane("XY").box(part_1_size, part_1_size, part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2: Cutout ---
cutout_size = 0.3645 * 0.3645
cutout_depth = 0.3
cutout = cq.Workplane("XY").box(cutout_size, cutout_size, cutout_depth)
# --- Coordinate System Transformation for Part 2 ---
cutout = cutout.rotate((0, 0, 0), (0, 0, 1), -90)
cutout = cutout.translate((0.17, 0.75, 0.0816))
# --- Part 3: Cutout 2 ---
cutout2_size = 0.3645 * 0.3645
cutout2_depth = 0.15
cutout2 = cq.Workplane("XY").box(cutout2_size, cutout2_size,
# Export
# 定义结果变量
result = cutout2
# 导出为STL文件
cq.exporters.export(result, "output_959.stl