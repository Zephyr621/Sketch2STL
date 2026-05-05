import cadquery as cq
# --- Part 1: Washer ---
outer_points = [
    (0.0, 0.2344),
    (0.375, 0.0),
    (0.75, 0.2344),
    (0.5357, 0.4286),
    (0.2493, 0.4286)
]
inner_points = [
    (0.3214, 0.2527),
    (0.2143, 0.2527),
    (0.3214, 0.2277),
    (0.6429, 0.2277),
    (0.6429, 0.4919),
    (0.3214, 0.4919)
]
sketch_scale = 0.75
extrude_depth = 0.0765
outer_points_scaled = [(x * sketch_scale, y * sketch_scale) for x, y in outer_points]
inner_points_scaled = [(x * sketch_scale, y * sketch_scale) for x, y in inner_points]
part_1 = (
    cq.Workplane("XY")
    .polyline(outer_points_scaled)
    .close()
    .add(cq.Workplane("XY").polyline(inner_
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1522.stl