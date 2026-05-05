import cadquery as cq
# --- Part 1: Cylinder ---
part_1_radius = 0.3261 * 0.6573  # Sketch radius scaled
part_1_height = 0.2629
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(-part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.1364))
# --- Part 2: Hole ---
part_2_radius = 0.375 * 0.75  # Sketch radius scaled
part_2_height = 0.1364
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(-part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), 180)
part_2 = part_2.translate((0, 0.5625, 0.1364))
# --- Part 3: Cut ---
part_3_radius = 0.375 * 0.75  # Sketch radius scaled
part_3_height = 0.1364
part_3 = cq.Workplane("XY").circle(part_3_radius).extrude(-part_3_height)
# --- Coordinate
# Export
# 定义结果变量
result = part_3
# 导出为STL文件
cq.exporters.export(result, "output_1182.stl