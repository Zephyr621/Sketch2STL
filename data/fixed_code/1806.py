import cadquery as cq
# --- Parameters from JSON ---
length = 0.75
width = 0.6495
height = 0.1291
sketch_scale = 0.75
# Scaled parameters
scaled_length = length * sketch_scale
scaled_width = width * sketch_scale
scaled_height = height
# --- Create the base cube ---
base_cube = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(scaled_length, 0)
    .lineTo(scaled_length / 2, scaled_width)
    .lineTo(0, scaled_width)
    .close()
)
# --- Extrude the base cube ---
result = base_cube.extrude(scaled_height)
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.exp
# 导出为STL文件
cq.exporters.export(result, "output_1806.stl