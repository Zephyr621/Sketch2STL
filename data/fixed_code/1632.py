import cadquery as cq
# --- Part 1: Cube with Circular Hole ---
part_1_size = 0.75 * 0.75  # Sketch size scaled
part_1_height = 0.4488
hole_center_x = 0.375 * 0.75
hole_center_y = 0.3516 * 0.75
hole_radius = 0.2904 * 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_size, part_1_size)
    .extrude(part_1_height)
    .faces(">Z").workplane()
    .moveTo(hole_center_x - part_1_size/2, hole_center_y - part_1_size/2)
    .circle(hole_radius)
    .cutThruAll()
)
# --- Part 2: Rect
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1632.stl