import cadquery as cq
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.75
# Scaled dimensions
scaled_0_0469 = 0.0469 * sketch_scale
scaled_0_1245 = 0.1245 * sketch_scale
scaled_0_2411 = 0.2411 * sketch_scale
scaled_0_3978 = 0.3978 * sketch_scale
scaled_0_75 = 0.75 * sketch_scale
scaled_0_4818 = 0.4818 * sketch_scale
scaled_0_5523 = 0.5523 * sketch_scale
scaled_0_6495 = 0.6495 * sketch_scale
scaled_0_6818 = 0.6818 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, scaled_0_0469)
    .lineTo(scaled_0_0469, 0.0)
    .lineTo(scaled_0_0469, scaled_0_0893)
    .lineTo(scaled_0_2411, scaled_0_0893)
    .lineTo(scaled_0_2411, scaled_0_1777)
    .lineTo(scaled_0_0469, scaled_0_
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2164.stl