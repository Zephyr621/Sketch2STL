import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.0225, 0.0)
    .lineTo(0.0225, 0.0511)
    .lineTo(0.0038, 0.0511)
    .lineTo(0.0038, 0.0511)
    .lineTo(0.0, 0.0511)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.75)
)
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.
cq.
cq.
cq.
cq.
cq.cq.exporters.export(assembly
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3511.stl