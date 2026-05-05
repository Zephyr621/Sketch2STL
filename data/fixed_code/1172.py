import cadquery as cq
# --- Part 1: Base Rectangular Prism with Cutout ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(0.3125 * 0.75, 0)
    .lineTo(0.3125 * 0.75, 0.1875 * 0.75)
    .lineTo(0.75 * 0.75, 0.1875 * 0.75)
    .lineTo(0.75 * 0.75, 0.375 * 0.75)
    .lineTo(0, 0.375 * 0.75)
    .close()
    .extrude(0.15)
)
# Create the cutout on the side of the base
cutout = (
    cq.Workplane("XY")
    .moveTo(0.3125 * 0.75, 0.1875 * 0.75)
    .lineTo(0.75 * 0.75, 0.1875 * 0.75)
    .lineTo(0.75 * 0.75, 0.375 * 0.75)
    .lineTo(0.3125 * 0.75, 0.375 * 0.75)
    .lineTo(0.3125 * 0.75, 0.1875 * 0.75)
    .close()
    .extrude
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1172.stl