import cadquery as cq
# --- Part 1: Rectangular Block with Holes ---
block_length = 0.75 * 0.75  # Scaled length
block_width = 0.4167 * 0.75  # Scaled width
block_height = 0.25
hole_radius = 0.0625 * 0.75  # Scaled radius
hole1_x = 0.2165 * 0.75  # Scaled x-coordinate
hole1_y = 0.0625 * 0.75  # Scaled y-coordinate
hole2_x = 0.625 * 0.75  # Scaled x-coordinate
hole2_y = 0.0625 * 0.75  # Scaled y-coordinate
part_1 = (
    cq.Workplane("XY")
    .rect(block_length, block_width)
    .extrude(block_height)
    .faces(">Z").workplane()
    .pushPoints([(hole1_x - block_length/2, hole1_y - block_width/2), (hole2_x - block_length/2, hole2_y - block_width/2)])
    .hole(hole_radius * 2)
)
# --- Part 2: Cube ---
cube_size = 0.5 * 0.5  # Scaled
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2677.stl