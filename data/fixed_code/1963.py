import cadquery as cq
# --- Part 1: Rectangular Block ---
length = 0.75 * 0.75  # Scaled length
width = 0.15 * 0.75  # Scaled width
height = 0.0875
part_1 = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Part 2: Cut Feature (Holes) ---
hole_size = 0.0536 * 0.6178
hole_depth = 0.0875
hole1_x = 0.0688 * 0.6178
hole2_x = 0.6847 * 0.6178
hole3_x = 0.6763 * 0.6178
hole4_x = 0.75 * 0.6178
hole5_y = 0.0937 * 0.6178
hole6_x = 0.6964 * 0.6178
# Create holes
part_2 = (
    part_1.faces(">Z")
    .workplane()
    .hole(2 * hole_size, clean=True)
)
# Apply translation
part_2 = part_2.translate((0, 0, 0.0875))
# Add holes to part 2
part_3 = (
# Export
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_1963.stl