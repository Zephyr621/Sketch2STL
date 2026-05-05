import cadquery as cq
# --- Part 1: L-shaped base ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.5196 * 0.75)
    .lineTo(0.0188 * 0.75, 0.5196 * 0.75)
    .lineTo(0.0188 * 0.75, 0.0)
    .lineTo(0.7347 * 0.75, 0.0)
    .lineTo(0.7347 * 0.75, 0.5196 * 0.75)
    .lineTo(0.7347 * 0.75, 0.75 * 0.75)
    .lineTo(0.0, 0.75 * 0.75)
    .close()
    .extrude(-0.1289)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
# --- Part 2: Rectangular Box ---
part_2 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.5196 * 0.4375)
    .lineTo(0.0188 * 0.4375, 0.0)
    .lineTo
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_833.stl