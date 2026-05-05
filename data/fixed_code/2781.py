import cadquery as cq
# --- Part 1: Support Bracket ---
length = 0.75 * 0.75  # Scaled length
width = 0.5217 * 0.75  # Scaled width
height = 0.0234  # Height
# Create the base rectangle
base_rect = cq.Workplane("XY").rect(length, width).extrude(height)
# Create the vertical extension (cutout)
extension_height = 0.0341 * 0.75  # Scaled height
extension_width = (0.75 - 2 * 0.0955) / (0.5217 - 0.2325)
extension_depth = 0.0197  # Depth
# Create the rectangular extension
extension = cq.Workplane("XY").rect(extension_width, extension_depth).extrude(height)
# Translate the extension to its correct position
extension = extension.translate((0, 0, height))
# Perform the cuts
part_1 = base_rect.cut(extension)
# Export the result to a STL file
cq.
# --- Assembly ---
assembly = part_1
# Export the assembly to a STL file
cq.
# 定义结果变量
result = extension
# 导出为STL文件
cq.exporters.export(result, "output_2781.stl