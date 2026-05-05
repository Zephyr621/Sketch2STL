import cadquery as cq
# --- Part 1: L-shaped CAD Model ---
sketch_scale = 0.75
extrude_depth = 0.3142 * 2  # Total extrusion depth (towards + opposite normal)
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(0.0577 * sketch_scale, 0)
    .lineTo(0.6972 * sketch_scale, 0)
    .lineTo(0.75 * sketch_scale, 0)
    .lineTo(0.75 * sketch_scale, 0.5062 * sketch_scale)
    .lineTo(0.6972 * sketch_scale, 0.5062 * sketch_scale)
    .lineTo(0.6972 * sketch_scale, 0.5303 * sketch_scale)
    .lineTo(0, 0.5303 * sketch_scale)
    .lineTo(0, 0)
    .close()
    .extrude(extrude_depth)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0,
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1453.stl