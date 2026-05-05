import cadquery as cq
from math import radians
# --- Part 1: Roders ---
rod_radius = 0.0039 * 0.0078  # Radius scaled
rod_height = 0.75
# Cylinder positions (scaled)
cylinder_positions = [
    (0.0039 * 0.0078, 0.0039 * 0.0078),
    (0.0039 * 0.0078, 0.7391 * 0.0078),
    (0.0039 * 0.0078, 0.7391 * 0.0078)
]
# Create the rods
rod1 = cq.Workplane("XY")
for x, y in cylinder_positions:
    rod1 = rod1.moveTo(x, y).circle(rod_radius).extrude(rod_height)
# --- Coordinate System Transformation for Part 1 ---
rod1 = rod1.rotate((0, 0, 0), (0, 0, 1), -90)
rod1 = rod1.translate((0, 0.75, 0))
# --- Assembly ---
assembly = rod1
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq
# 定义结果变量
result = rod1
# 导出为STL文件
cq.exporters.export(result, "output_3096.stl