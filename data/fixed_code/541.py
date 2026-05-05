import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.0937 * 0.0938, 0.0)
    .lineTo(0.0937 * 0.0938, 0.0938 * 0.0938)
    .lineTo(0.0, 0.0938 * 0.0938)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(-0.75)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
#part_1 = part_1.translate((0, 0, 0)) # Translation not needed
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.
cq.
cq.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_541.stl