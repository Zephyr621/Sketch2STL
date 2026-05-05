import cadquery as cq
# --- Part 1: Cylinder ---
part_1_radius = 0.1033 * 0.2333  # Sketch radius scaled
part_1_height = 0.3667
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(-part_1_height)
part_1 = part_1.translate((0, 0, 0.3667))
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2: Cylinder ---
part_2_radius = 0.1033 * 0.2333  # Sketch radius scaled
part_2_height = 0.1583
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(-part_2_height)
part_2 = part_2.translate((0.2067, 0.2067, 0.3667))
# --- Part 3: Cylinder ---
part_3_radius = 0.1033 * 0.2333  # Sketch radius scaled
part_3_height = 0.001.
# Export
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_2647.stl