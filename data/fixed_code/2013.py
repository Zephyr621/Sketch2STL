import cadquery as cq
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_height = 0.3
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Part 2: Recessed Top ---
part_2_outer_radius = 0.375 * 0.75  # Outer radius scaled
part_2_inner_radius = 0.33 * 0.75
part_2_height = 0.3
part_2 = (
    cq.Workplane("XY")
    .workplane(offset=0.3)  # Move to the top of the cylinder
    .moveTo(0.15, 0.15)  # Create a smaller circle for the recess
    .circle(part_2_outer_radius)
    .extrude(-part_2_height)  # Extrude downwards
)
# --- Assembly ---
assembly = part_1.union(part_2)
# --- Export to STL ---
# --- Export to STL ---
# --- Export to STL ---
# --- Export to
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_2013.stl