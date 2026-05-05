import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cube with Rounded Edges ---
length = 0.75 * 0.75  # Scaled length
width = 0.5625 * 0.75  # Scaled width
height = 0.0937
# Create the basic cube
cube = cq.Workplane("XY").box(length, width, height)
# Apply fillets to all edges
fillet_radius = min(length, width, height) / 10  # Adjust as needed; avoid large values
cube = cube.edges().fillet(fillet_radius)
# --- Coordinate System Transformation for Part 1 ---
cube = cube.rotate((0, 0, 0), (0, 0, 1), -90)
cube = cube.translate((0, 0.0937, 0))
# --- Assembly ---
assembly = cube
# Export to STL
cq.
# Export to STL
cq.
# --- Export to STL ---
cq.
# Export to STL
cq.
# --- Coordinate System Transformation for Part 1 ---
# 定义结果变量
result = cube
# 导出为STL文件
cq.exporters.export(result, "output_155.stl