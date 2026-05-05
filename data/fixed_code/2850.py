import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.125 * 0.75)
    .lineTo(0.1875 * 0.75, 0.125 * 0.75)
    .lineTo(0.1875 * 0.75, 0.4375 * 0.75)
    .lineTo(0.0, 0.4375 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.1667)
)
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.
cq.
cq.exp
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2850.stl