import cadquery as cq
# --- Part 1: Cylinder ---
part_1_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_height = 0.45
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Part 2: Cut Cylinder ---
part_2_radius = 0.1875 * 0.5625  # Sketch radius scaled
part_2_height = 0.45
part_2 = (
    cq.Workplane("XY")
    .workplane(offset=0.45)  # Move to the top of part_1
    .moveTo(0.15, 0.15)  # Translate to the center of the circle
    .circle(part_2_radius)
    .extrude(-part_2_height)  # Extrude downwards for cutting
)
# --- Assembly ---
result = part_1.cut(part_2)
cq.
# --- Export STL ---
cq.
# --- Export Spherical Top ---
sketch_scale = 0.5625
# Define the points for the sketch
points = [
    (0.0, 0.0841),
    (0.0851, 0.0),
    (0.6681
# 导出为STL文件
cq.exporters.export(result, "output_1947.stl