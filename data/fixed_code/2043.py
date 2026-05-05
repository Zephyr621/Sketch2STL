import cadquery as cq
# --- Parameters from JSON ---
outer_size = 0.75 * 0.75  # Scaled outer square size
inner_offset = 0.0312 * 0.75  # Scaled inner offset (0.0312 - 0.0038)
height = 0.15
# --- Create the outer square ---
outer_square = cq.Workplane("XY").rect(outer_size, outer_size).extrude(height)
# --- Create the inner square (hole) ---
inner_square = cq.Workplane("XY").rect(outer_size - 2 * inner_offset, outer_size - 2 * inner_offset).extrude(height)
# --- Cut the inner square from the outer square ---
result = outer_square.cut(inner_square)
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to
# 导出为STL文件
cq.exporters.export(result, "output_2043.stl