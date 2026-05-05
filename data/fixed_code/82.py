import cadquery as cq
# --- Part 1: Cube with Circular Hole ---
part_1_size = 0.75 * 0.75  # Scaled size
part_1_hole_radius = 0.1125 * 0.75  # Scaled radius
part_1_height = 0.225
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_size, part_1_size)
    .extrude(-part_1_height)  # Extrude downwards
    .faces(">Z").workplane()
    .circle(part_1_hole_radius)
    .cutThruAll()
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Part 2: Cut Feature ---
part_2_size = 0.75 * 0.75  # Scaled size
part_2_depth = 0.75
part_2 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(0.375 * 0.75, 0)
    .lineTo(0.375 * 0.75, 0.75 * 0.75)
    .lineTo(0, 0.75 * 0.75)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_82.stl