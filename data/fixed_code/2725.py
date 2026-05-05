import cadquery as cq
# --- Parameters from JSON ---
length = 0.0234 * 0.0234  # Scaled length
width = 0.0129 * 0.0234   # Scaled width
height = 0.75
hole_radius = 0.0059 * 0.0234  # Scaled radius
hole_center_x1 = 0.0117 * 0.0234  # Scaled center x
hole_center_y1 = 0.0117 * 0.0234  # Scaled center y
hole_center_x2 = 0.0117 * 0.0234  # Scaled center x
hole_center_y2 = 0.0117 * 0.0234  # Scaled center y
# --- Create the base rectangular block ---
block = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Create the holes ---
block = (
    block.faces(">Z")
    .workplane()
    .hole(2 * hole_radius)
    .faces(">Z")
    .workplane()
    .moveTo(hole_center_x1 - length/2, hole_center_y1 - width/2)
    .hole(2 * hole_radius)
)
block = (
    block.faces(">X")
    .workplane()
    .moveTo(hole_center_x2 -
# Export
# 定义结果变量
result = block
# 导出为STL文件
cq.exporters.export(result, "output_2725.stl