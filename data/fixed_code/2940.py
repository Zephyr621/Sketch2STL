import cadquery as cq
# --- Part 1: V-shaped Object ---
sketch_scale = 0.75
extrude_depth = 0.75
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * sketch_scale, 0.0)
    .lineTo(0.75 * sketch_scale, 0.15 * sketch_scale)
    .lineTo(0.5 * sketch_scale, 0.2961 * sketch_scale)
    .lineTo(0.2312 * sketch_scale, 0.2891 * sketch_scale)
    .lineTo(0.0, 0.1406 * sketch_scale)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(extrude_depth)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
cq
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2940.stl