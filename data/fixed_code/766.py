import cadquery as cq
# --- Part 1: Rectangular Prism ---
part_1_width = 0.1896 * 0.1896  # Scaled width
part_1_length = 0.1896 * 0.1896 # Scaled length
part_1_height = 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_width, part_1_length)
    .extrude(-part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.1896, 0.0, 0.0))
# --- Part 2: Vertical Supports ---
support_width = 0.0214 * 0.5971  # Scaled width
support_length = 0.5971 * 0.5971 # Scaled length
support_height = 0.75
# Create a function to generate a single support
def create_supports():
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_766.stl