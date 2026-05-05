import cadquery as cq
# --- Part 1: Cube with Cutout ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.375 * 0.75)
    .lineTo(0.7031 * 0.75, 0.375 * 0.75)
    .lineTo(0.7031 * 0.75, 0.7031 * 0.75)
    .lineTo(0.0, 0.7031 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(-0.45)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Part 2: Cylindrical Objects ---
cylinder_radius = 0.0117 * 0.7031
cylinder_height = 0.2143
cylinder_locations = [
    (0.0117 * 0.7031, 0.0117 * 0.7031),
    (0.0117 * 0.7031, 0.7031 * 0.7
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1571.stl