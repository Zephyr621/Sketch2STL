import cadquery as cq
# --- Part 1: Cube with Cutout ---
outer_rect_size = 0.75 * 0.75  # Scaled size
inner_rect_offset = 0.0469 * 0.75  # Scaled offset
extrude_depth = 0.5625
part_1 = (
    cq.Workplane("XY")
    .rect(outer_rect_size, outer_rect_size)
    .extrude(extrude_depth)
    .faces(">Z")
    .workplane()
    .rect(outer_rect_size - 2 * inner_rect_offset, outer_rect_size - 2 * inner_rect_offset)
    .cutThruAll()
)
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.exp
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2420.stl