import cadquery as cq
# --- Part 1: Rectangular Plate with Holes ---
part_1_length = 0.7005 * 0.7005  # Scaled length
part_1_width = 0.1845 * 0.7005  # Scaled width
part_1_height = 0.0269
hole_radius = 0.0147 * 0.7005  # Scaled radius
hole_center_1 = (0.1797 * 0.7005 - part_1_length/2, 0.0938 * 0.7005 - part_1_width/2)  # Scaled and centered
hole_center_2 = (0.5795 * 0.7005 - part_1_length/2, 0.0938 * 0.7005 - part_1_width/2)  # Scaled and centered
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
    .faces(">Z").workplane()
    .pushPoints([hole_center_1, hole_center_2])
    .hole(2 * hole_radius)
)
# --- Coordinate System Transformation for Part 1 ---
part_1
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3441.stl