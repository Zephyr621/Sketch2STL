import cadquery as cq
from math import tan, radians
# --- Parameters from JSON ---
cylinder_radius = 0.375 * 0.75  # Scaled radius
hexagon_points = [
    (0.125 * 0.75 - cylinder_radius, 0.25 * 0.75 - cylinder_radius),
    (0.375 * 0.75 - cylinder_radius, 0.125 * 0.75 - cylinder_radius),
    (0.5 * 0.75 - cylinder_radius, 0.25 * 0.75 - cylinder_radius)
]
hole1_center = (0.3125 * 0.75 - cylinder_radius, 0.125 * 0.75 - cylinder_radius)
hole2_center = (0.625 * 0.75 - cylinder_radius, 0.375 * 0.75 - cylinder_radius)
# --- Create Cylinder ---
cylinder = cq.Workplane("XY").circle(cylinder_radius).extrude(cylinder_height)
# --- Create Hexagon ---
hexagon = cq.Workplane("XY").polyline(hexagon_points).close().extrude(cylinder_height + 0.1)  # Extrude slightly more to ensure full cut
# --- Cut Hole ---
hole = cq.Workplane("XY").moveTo(hole1_center[0], hole1_center[1]).circle(hole_radius).extrude(cylinder_height + 0.1)  # Extrude
# Export
# 定义结果变量
result = hole
# 导出为STL文件
cq.exporters.export(result, "output_2570.stl