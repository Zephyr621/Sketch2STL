import cadquery as cq
import math
from cadquery.vis import show
# --- Parameters from JSON ---
length = 0.75
width = 0.3214
height = 0.1071
sketch_scale = 0.75
hole1_center = (0.1536 * sketch_scale, 0.1607 * sketch_scale)
hole2_center = (0.5527 * sketch_scale, 0.1607 * sketch_scale)
hole_radius = 0.0529 * sketch_scale
# --- Create the base plate with rounded corners ---
plate = (
    cq.Workplane("XY")
    .moveTo(0.375 * sketch_scale, 0)
    .lineTo(0.75 * sketch_scale, 0)
    .lineTo(0.75 * sketch_scale, 0.3214 * sketch_scale)
    .threePointArc((0.6149 * sketch_scale, 0.3214 * sketch_scale), (0.375 * sketch_scale, 0.3214 * sketch_scale))
    .close()
    .extrude(height)
)
# --- Add holes ---
plate = (
    plate.faces(">Z")
    .workplane()
    .pushPoints([
        (hole1_center[0] - (length
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_128.stl