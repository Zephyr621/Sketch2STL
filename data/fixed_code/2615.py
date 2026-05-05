import cadquery as cq
# --- Part 1: Rectangular Prism with Hole ---
sketch_scale = 0.75
length = 0.75 * sketch_scale
width = 0.45 * sketch_scale
height = 0.15
hole_center_x = 0.3 * sketch_scale
hole_center_y = 0.225 * sketch_scale
hole_radius = 0.1125 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
    .faces(">Z").workplane()
    .moveTo(hole_center_x - length/2, hole_center_y - width/2)
    .circle(hole_radius)
    .cutThruAll()
)
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# Export to STL
cq.
#
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2615.stl