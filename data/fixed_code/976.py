import cadquery as cq
# --- Parameters from JSON ---
length = 0.75
width = 0.1811
height = 0.0465
sketch_scale = 0.75
hole1_center = (0.0441, 0.0443)
hole2_center = (0.6954, 0.0443)
hole3_center = (0.7134, 0.0443)
hole_radius = 0.0203
# --- Create the base rectangle ---
rect = cq.Workplane("XY").rect(length * sketch_scale, width * sketch_scale).extrude(height)
# --- Create the holes ---
hole1 = cq.Workplane("XY").moveTo(hole1_center[0] - (length * sketch_scale)/2, hole1_center[1] - (width * sketch_scale)/2).circle(hole_radius * sketch_scale).extrude(height + 0.1)
hole2 = cq.Workplane("XY").moveTo(hole2_center[0] - (length * sketch_scale)/2, hole2_center[1] - (width * sketch_scale)/2).circle(hole_radius * sketch_scale).extrude(height + 0.1)
hole3 = cq.Workplane("XY").moveTo(hole3_center[0] - (length * sketch_scale)/2, hole3_center[1] - (width * sketch_scale)/2).
# Export
# 定义结果变量
result = hole3
# 导出为STL文件
cq.exporters.export(result, "output_976.stl