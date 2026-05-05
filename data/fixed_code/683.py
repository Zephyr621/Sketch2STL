import cadquery as cq
# --- Part 1: Washer ---
outer_radius = 0.375 * 0.75  # Sketch radius scaled
inner_radius = 0.1714 * 0.75  # Inner hole radius scaled
height = 0.0536
washer = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .extrude(height)
    .faces(">Z")
    .workplane()
    .circle(inner_radius)
    .cutThruAll()
)
# --- Coordinate System Transformation for Part 1 ---
washer = washer.rotate((0, 0, 0), (0, 0, 1), -90)
washer = washer.translate((0, 0.0536, 0))
# --- Export to STL ---
cq.
cq.
cq.
cq.
cq.exporters.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_683.stl