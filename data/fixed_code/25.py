import cadquery as cq
# --- Part 1: L-shaped CAD Model ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.625 * 0.625, 0.0)
    .lineTo(0.625 * 0.625, 0.25 * 0.625)
    .lineTo(0.375 * 0.625, 0.25 * 0.625)
    .lineTo(0.125 * 0.625, 0.625 * 0.625)
    .lineTo(0.0, 0.625 * 0.625)
    .close()
    .extrude(0.75)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2: Cylinder (Cut) ---
part_2_radius = 0.3125 * 0.625  # Sketch radius scaled
part_2_height = 0.75
part_2 = (
    cq.Workplane("XY")
    .workplane()
    .moveTo(0.125 * 0.625, 0.25 * 0.625)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_25.stl