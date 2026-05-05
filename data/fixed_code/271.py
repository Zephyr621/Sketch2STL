import cadquery as cq
# --- Part 1: Cube ---
part_1_size = 0.75 * 0.75  # Sketch size scaled
part_1_height = 0.375
part_1 = cq.Workplane("XY").rect(part_1_size, part_1_size).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2: Hole ---
hole_size = 0.3125 * 0.4648  # Sketch size scaled
hole_depth = 0.1875
part_2 = cq.Workplane("XY").rect(hole_size, hole_size).extrude(-hole_depth)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.1563, 0, 0.1562))
# --- Part 3: Cut ---
cut_size = 0.225 * 0.225  # Sketch size scaled
cut_depth = 0.0938
part_3 = cq.Workplane("XY").rect
# Export
# 定义结果变量
result = part_3
# 导出为STL文件
cq.exporters.export(result, "output_271.stl