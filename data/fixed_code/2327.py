import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.0844)
    .lineTo(0.6198, 0.0844)
    .lineTo(0.6198, 0.1089)
    .lineTo(0.75, 0.1089)
    .lineTo(0.75, 0.1743)
    .lineTo(0.6198, 0.1743)
    .lineTo(0.6198, 0.0844)
    .lineTo(0.2813, 0.0844)
    .lineTo(0.2813, 0.0844)
    .lineTo(0.0, 0.0844)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(-0.375)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Assembly ---
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2327.stl