import cadquery as cq
# --- Part 1: Base ---
part_1 = (
    cq.Workplane("XY")
    .rect(0.75 * 0.75, 0.1083 * 0.75)
    .extrude(-0.1833)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Part 2: Side Walls ---
part_2 = (
    cq.Workplane("XY")
    .rect(0.6429 * 0.6429, 0.6429 * 0.6429)
    .extrude(-0.0117)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.0313, 0, 0.0313))
# --- Part 3: Side Walls ---
part_3 = (
    cq.Workplane("XY")
    .rect(0.7179 * 0.7179, 0.
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2522.stl