import cadquery as cq
# --- Parameters from JSON ---
length = 0.75 * 0.75  # Scaled length
width = 0.4688 * 0.75  # Scaled width
height = 0.0156  # Height
hole_radius = 0.0094 * 0.75  # Scaled radius
hole_center_x1 = 0.1875 * 0.75  # Scaled center x
hole_center_y1 = 0.1944 * 0.75  # Scaled center y
hole_center_x2 = 0.5625 * 0.75  # Scaled center x
hole_center_y2 = 0.1944 * 0.75  # Scaled center y
# --- Create the base rectangular plate ---
plate = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
)
# --- Create the hole ---
plate = (
    plate.faces(">Z")
    .workplane()
    .moveTo(hole_center_x1 - length/2, hole_center_y1 - width/2)
    .circle(hole_radius)
    .cutThruAll()
)
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.cq.exporters.export(plate,
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2461.stl