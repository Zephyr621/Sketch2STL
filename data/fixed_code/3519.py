import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder with Protrusion ---
part_1_radius = 0.0767 * 0.75  # Sketch radius scaled
part_1_height = 0.0185
# Create the base cylinder
base_cylinder = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# Create the protrusion sketch (hole)
protrusion_sketch = (
    cq.Workplane("XY")
    .moveTo(0.0767 * 0.75, 0.0767 * 0.75)
    .lineTo(0.6562 * 0.75, 0.0767 * 0.75)
    .lineTo(0.6562 * 0.75, 0.1442 * 0.75)
    .lineTo(0.0767 * 0.75, 0.1442 * 0.75)
    .close()
)
# Extrude the protrusion to create the hole
protrusion = protrusion_sketch.extrude(part_1_height + 0.001) #Extrude slightly more than half a unit
# Cut the hole from the base cylinder
result = base_cylinder.cut(protrusion)
cq.
# Export
# 导出为STL文件
cq.exporters.export(result, "output_3519.stl