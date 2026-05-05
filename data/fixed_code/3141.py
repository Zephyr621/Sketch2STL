import cadquery as cq
# --- Part 1: L-shaped CAD Model ---
sketch_scale = 0.75
extrude_depth = 0.1875
# Scaled dimensions
scaled_width = 0.75 * sketch_scale
scaled_height = 0.4687 * sketch_scale
scaled_thickness = 0.0937 * sketch_scale
# Create the L-shape profile
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(scaled_width, 0)
    .lineTo(scaled_width, scaled_thickness)
    .lineTo(scaled_thickness, scaled_thickness)
    .lineTo(scaled_thickness, scaled_thickness)
    .lineTo(0, scaled_thickness)
    .lineTo(0, 0)
    .close()
    .moveTo(scaled_width - scaled_thickness, 0)
    .lineTo(scaled_width - scaled_thickness, scaled_thickness)
    .lineTo(scaled_width - scaled_thickness, scaled_thickness + scaled_thickness)
    .lineTo(scaled_width - scaled_thickness + scaled_thickness, scaled_thickness)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3141.stl