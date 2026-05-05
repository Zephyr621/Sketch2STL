import cadquery as cq
# --- Part 1: Cube with Circular Hole ---
cube_size = 0.75 * 0.75  # Scaled cube size
hole_radius = 0.2269 * 0.75  # Scaled hole radius
extrude_depth = 0.1293
part_1 = (
    cq.Workplane("XY")
    .rect(cube_size, cube_size)
    .extrude(extrude_depth)
    .faces(">Z").workplane()
    .circle(hole_radius)
    .cutThruAll()
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
cq.
cq.
cq.
# 导出为STL文件
cq.exporters.export(result, "output_1754.stl