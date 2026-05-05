import cadquery as cq
# --- Parameters from JSON ---
length = 0.75
width = 0.5563
height = 0.0214
sketch_scale = 0.75
hole1_center = (0.0457 * sketch_scale, 0.1907 * sketch_scale)
hole2_center = (0.5357 * sketch_scale, 0.1907 * sketch_scale)
hole3_center = (0.6964 * sketch_scale, 0.0982 * sketch_scale)
hole4_center = (0.7286 * sketch_scale, 0.1907 * sketch_scale)
hole5_center = (0.75 * sketch_scale, 0.5563 * sketch_scale)
hole6_center = (0.6964 * sketch_scale, 0.5621 * sketch_scale)
# --- Create the base rectangular plate ---
plate = cq.Workplane("XY").rect(length * sketch_scale, width * sketch_scale).extrude(height)
# --- Add holes ---
plate = (
    plate.faces(">Z")
    .workplane()
    .pushPoints([
        (hole1_center[0] - (length * sketch_scale)/2, hole1_center[1] - (width * sketch_scale)/2),
        (hole2_center[0] - (length * sketch_scale)/2, hole2_center[1] -
# Export
# 定义结果变量
result = plate
# 导出为STL文件
cq.exporters.export(result, "output_2189.stl