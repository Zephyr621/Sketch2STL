import cadquery as cq
# --- Parameters from JSON ---
length = 0.75 * 0.75  # Scaled length
width = 0.6429 * 0.75  # Scaled width
height = 0.3159
hole_radius = 0.0854 * 0.75  # Scaled radius
hole_center1 = (0.1333 * 0.75 - length/2, 0.1071 * 0.75 - width/2)  # Scaled and centered
hole_center2 = (0.6159 * 0.75 - length/2, 0.6429 * 0.75 - width/2)  # Scaled and centered
# --- Create Cube ---
cube = cq.Workplane("XY").rect(length, width).extrude(height)
# --- Create Holes ---
cube = (
    cube.faces(">Z")
    .workplane()
    .pushPoints([hole_center1])
    .hole(2 * hole_radius)
)
cube = (
    cube.faces(">Z")
    .workplane()
    .pushPoints([hole_center2])
    .hole(2 * hole_radius)
)
# --- Apply Transformations ---
cube = cube.rotate((0, 0, 0), (0,
# Export
# 定义结果变量
result = cube
# 导出为STL文件
cq.exporters.export(result, "output_1320.stl