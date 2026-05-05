import cadquery as cq
from cadquery.vis import show
# --- Part 1: Arrow Head ---
sketch_scale = 0.75
extrude_depth = 0.0296 * 2  # Total extrusion depth (towards + opposite normal)
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0026 * sketch_scale)
    .lineTo(0.0, 0.1765 * sketch_scale)
    .threePointArc((0.0869 * sketch_scale, 0.1748 * sketch_scale), (0.0026 * sketch_scale, 0.1765 * sketch_scale))
    .lineTo(0.0026 * sketch_scale, 0.3797 * sketch_scale)
    .threePointArc((0.0869 * sketch_scale, 0.2669 * sketch_scale), (0.0, 0.1765 * sketch_scale))
    .close()
    .extrude(extrude_depth)
)
# --- Assembly ---
assembly = part_1
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2450.stl