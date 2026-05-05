import cadquery as cq
# --- Part 1: L-shaped Base ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(0.75 * 0.75, 0)
    .lineTo(0.75 * 0.75, 0.0937 * 0.75)
    .lineTo(0.5625 * 0.75, 0.0937 * 0.75)
    .lineTo(0.5625 * 0.75, 0.4688 * 0.75)
    .lineTo(0.1875 * 0.75, 0.4688 * 0.75)
    .lineTo(0.1875 * 0.75, 0.2812 * 0.75)
    .lineTo(0.0, 0.2812 * 0.75)
    .close()
    .extrude(0.5625)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.5625, 0))
# --- Part 2: Rectangular Protrusion ---
part_2 = (
    cq.Workplane("XY")
    .rect(0.375 * 0.375, 0.1875 * 0.375)
    .extrude(-0.
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3026.stl