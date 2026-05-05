import cadquery as cq
# --- Part 1: Rectangular Plate ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.2906 * 0.75, 0.0)
    .lineTo(0.2906 * 0.75, 0.0156 * 0.75)
    .lineTo(0.0, 0.0156 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0094)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0094, 0))
# --- Part 2: Cut Feature ---
cut_sketch = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.2906 * 0.75, 0.0)
    .lineTo(0.2906 * 0.75, 0.0156 * 0.75)
    .lineTo(0.0, 0.0156 * 0.75)
    .lineTo(0.
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1231.stl