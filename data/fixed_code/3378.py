import cadquery as cq
# --- Part 1: Cube with Cutout ---
length = 0.75 * 0.75  # Scaled length
width = 0.5529 * 0.75  # Scaled width
height = 0.2509
cutout_x1 = 0.1289 * 0.75
cutout_y1 = 0.2703 * 0.75
cutout_x2 = 0.6048 * 0.75
cutout_y2 = 0.4286 * 0.75
cutout_x3 = 0.5396 * 0.75
cutout_y3 = 0.2703 * 0.75
cutout_x4 = 0.6071 * 0.75
cutout_y4 = 0.2703 * 0.75
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(length, 0)
    .lineTo(length, width)
    .lineTo(0.5357 * 0.75, width)
    .lineTo(0.5357 * 0.75, 0.5357 * 0.75)
    .lineTo(0, 0.5357 * 0.75)
    .close()
    .extrude(height)
)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3378.stl