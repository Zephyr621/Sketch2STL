import cadquery as cq
# --- Part 1: Base with Protrusion ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.4687)
    .lineTo(0.5625, 0.4687)
    .lineTo(0.5625, 0.2188)
    .lineTo(0.1875, 0.2188)
    .lineTo(0.1875, 0.4687)
    .lineTo(0.0, 0.4687)
    .close()
    .extrude(0.4018 * 0.75)
)
# --- Part 2: Vertical Extension ---
part_2_sketch_scale = 0.6526
part_2 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.0012 * part_2_sketch_scale, 0.0)
    .lineTo(0.0012 * part_2_sketch_scale, 0.3446 * part_2_sketch_scale)
    .lineTo(0.0, 0.3446 * part_2_sketch_scale)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2798.stl