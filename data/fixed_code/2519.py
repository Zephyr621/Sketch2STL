import cadquery as cq
# --- Parameters from JSON ---
outer_size = 0.75 * 0.75  # Scaled
inner_offset = 0.0156 * 0.75  # Scaled
height = 0.0313
hole_size = (0.5391 - 0.0156) * 0.75  # Scaled
hole_x = 0.7187 * 0.75  # Scaled
hole_y = 0.0156 * 0.75  # Scaled
extrusion_depth = height
# --- Create the base square with a hole ---
base = cq.Workplane("XY").rect(outer_size, outer_size).extrude(extrusion_depth)
# --- Cut the inner square from the outer square ---
result = base.cut(cq.Workplane("XY").rect(inner_size, inner_size).translate((hole_x - outer_size/2 + inner_offset, hole_y - outer_size/2 + inner_offset, 0)).extrude(extrusion_depth))
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export
# 导出为STL文件
cq.exporters.export(result, "output_2519.stl