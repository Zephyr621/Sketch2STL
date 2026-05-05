import cadquery as cq
# --- Part 1: Cube with Cutout ---
sketch_scale = 0.75
length = 0.75 * sketch_scale
width = 0.4687 * sketch_scale
height = 0.3633
cutout_x1 = 0.1512 * sketch_scale
cutout_y1 = 0.1875 * sketch_scale
cutout_x2 = 0.5925 * sketch_scale
cutout_y2 = 0.1365 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(length, 0)
    .lineTo(length, width)
    .lineTo(cutout_x1, width)
    .lineTo(cutout_x2, 0)
    .close()
    .extrude(height)
)
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# --- Export to STL ---
cq.
# Export to STL
cq.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3062.stl