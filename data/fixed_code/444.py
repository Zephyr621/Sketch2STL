import cadquery as cq
# --- Part 1: Cube with Square Opening ---
part_1_size = 0.75 * 0.75  # Sketch size scaled
part_1_thickness = 0.75
part_1 = cq.Workplane("XY").rect(part_1_size, part_1_size).extrude(part_1_thickness)
# --- Part 2: Square Plate (Cut) ---
part_2_size = 0.7188 * 0.7188  # Sketch size scaled
part_2_thickness = 0.0247
part_2 = cq.Workplane("XY").rect(part_2_size, part_2_size).extrude(-part_2_thickness)
part_2 = part_2.translate((0, 0, part_1_thickness))
# --- Part 3: Square Plate (Cut) ---
part_3_size = 0.7188 * 0.7188  # Sketch size scaled
part_3_thickness = 0.0247
part_3 = cq.Workplane("XY").rect(part_3_size, part_3_size).extrude(-part_3_thickness)
part_3 = part_3.translate((0.0184, 0.0184, part_1
# Export
# 定义结果变量
result = part_3
# 导出为STL文件
cq.exporters.export(result, "output_444.stl