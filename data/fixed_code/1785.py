import cadquery as cq
# --- Part 1: Cube with Cutouts ---
sketch_scale = 0.75
length = 0.75 * sketch_scale
width = 0.2458 * sketch_scale
height = 0.05
# Hole parameters (scaled)
hole1_x = 0.0728 * sketch_scale
hole1_y = 0.0923 * sketch_scale
hole2_x = 0.6704 * sketch_scale
hole2_y = 0.0923 * sketch_scale
hole3_x = 0.6893 * sketch_scale
hole3_y = 0.0923 * sketch_scale
hole4_x = 0.7298 * sketch_scale
hole4_y = 0.0923 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(length, 0)
    .lineTo(length, width)
    .lineTo(0, width)
    .close()
    .extrude(height)
)
# Create holes
part_1 = (
    part_1.faces(">Z")
    .workplane()
    .pushPoints([(hole1_x - length/2, hole1_y
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1785.stl