import cadquery as cq
from cadquery import exporters
# --- Part 1: Rectangular Base ---
base_length = 0.75 * 0.75  # Scaled length
base_width = 0.0417 * 0.75  # Scaled width
base_height = 0.015
part_1 = cq.Workplane("XY").rect(base_length, base_width).extrude(base_height)
# --- Part 2: Cut (Cylinder) ---
cut_radius = 0.0188 * 0.0375  # Scaled radius
cut_depth = 0.015
part_2 = cq.Workplane("XY").circle(cut_radius).extrude(-cut_depth)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0.0188, 0.0188, base_height))
# --- Assembly: Cut Part 2 from Part 1 ---
result = part_1.cut(part_2)
# --- Export to STL ---
# --- Export to STL ---
# --- Export to STL ---
# --- Export to STL ---
exporters.
# 导出为STL文件
cq.exporters.export(result, "output_906.stl