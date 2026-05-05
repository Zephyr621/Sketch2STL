import cadquery as cq
# --- Part 1: Rectangular Object ---
length = 0.75 * 0.75  # Scaled length
width = 0.5172 * 0.75  # Scaled width
height = 0.0383
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.0188))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# --- Export to STL ---
cq.
# Export to STL
cq.
# --- Fillet Edges ---
edge_radius = min(length, width) / 10  # Example fillet radius, adjust as needed
try:
    assembly = assembly.edges("|Z").fillet(edge_radius)
except:
    print("Fillet operation failed, proceeding without fillets.")
# ---
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3509.stl