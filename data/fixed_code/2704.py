import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0013)
    .lineTo(0.0012, 0.0013)
    .lineTo(0.0012, 0.1182)
    .lineTo(0.7174, 0.1182)
    .lineTo(0.7174, 0.2143)
    .lineTo(0.75, 0.2143)
    .lineTo(0.75, 0.2344)
    .lineTo(0.7174, 0.2344)
    .lineTo(0.7174, 0.1182)
    .lineTo(0.7174, 0.0893)
    .lineTo(0.7499, 0.0893)
    .lineTo(0.7499, 0.2344)
    .lineTo(0.0013, 0.2344)
    .lineTo(0.0013, 0.0893)
    .lineTo(0.0, 0.0893)
    .lineTo(0.0, 0.0013)
    .close()
    .extr
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2704.stl