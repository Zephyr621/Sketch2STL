import cadquery as cq
# --- Part 1: U-shaped Object ---
sketch_scale = 0.75
extrude_depth = 0.375 * 2  # Total extrusion depth (towards + opposite normal)
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.375 * sketch_scale, 0.0)
    .lineTo(0.375 * sketch_scale, 0.3788 * sketch_scale)
    .lineTo(0.0, 0.3788 * sketch_scale)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(extrude_depth)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.375 * sketch_scale, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# Export to STL
cq.
# --- Final Result ---
result = assembly
# 导出为STL文件
cq.exporters.export(result, "output_2586.stl