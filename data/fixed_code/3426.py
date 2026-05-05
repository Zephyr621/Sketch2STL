import cadquery as cq
# --- Part 1: Cube with Rounded Edges ---
length = 0.75 * 0.75  # Scaled length
width = 0.75 * 0.75   # Scaled width
height = 0.1875 + 0.1875  # Total height from extrusion
# Create the basic cube
cube = cq.Workplane("XY").box(length, width, height)
# Apply fillets to all edges
fillet_radius = min(length, width, height) / 10  # Adjust as needed
cube = cube.edges().fillet(fillet_radius)
# --- Coordinate System Transformation for Part 1 ---
cube = cube.rotate((0, 0, 0), (0, 0, 1), -90)
cube = cube.translate((0, 0.375, 0))
# --- Export to STL ---
cq.
# Export to STL
cq.
# --- Final Result ---
result = cube
cq.
cq.
# Export to STL
cq.exporters
# 导出为STL文件
cq.exporters.export(result, "output_3426.stl