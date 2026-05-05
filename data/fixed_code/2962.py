import cadquery as cq
# --- Parameters from JSON ---
length = 0.75
width = 0.4773
height = 0.0148
sketch_scale = 0.75
hole1_center = (0.0844 * sketch_scale, 0.1719 * sketch_scale)
hole2_center = (0.5751 * sketch_scale, 0.1719 * sketch_scale)
hole3_center = (0.5751 * sketch_scale, 0.4773 * sketch_scale)
hole_radius = 0.0089 * sketch_scale
# --- Create the base rectangular block ---
rect_length = length * sketch_scale
rect_width = width * sketch_scale
block = cq.Workplane("XY").rect(rect_length, rect_width).extrude(height)
# --- Create the holes ---
block = (
    block.faces(">Z")
    .workplane()
    .pushPoints([hole1_center])
    .hole(2 * hole_radius)
    .faces(">Z")
    .workplane()
    .pushPoints([hole2_center])
    .hole(2 * hole_radius)
    .faces(">Z")
    .workplane()
    .pushPoints([hole3_center])
    .hole(2 * hole_radius)
)
# --- Apply rotation and translation
# Export
# 定义结果变量
result = block
# 导出为STL文件
cq.exporters.export(result, "output_2962.stl