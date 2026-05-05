import cadquery as cq
# --- Part 1: Rectangular Object with Cutout ---
length = 0.75 * 0.75  # Scaled length
width = 0.3682 * 0.75  # Scaled width
height = 0.2143
cutout_x_min = 0.0808 * 0.75
cutout_y_min = 0.0577 * 0.75
cutout_x_max = 0.6963 * 0.75
cutout_y_max = 0.1879 * 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
)
# Create the cutout sketch
cutout_sketch = (
    cq.Workplane("XY")
    .moveTo(cutout_x_min - length/2, cutout_y_min - width/2)
    .lineTo(cutout_x_max - length/2, cutout_y_min - width/2)
    .lineTo(cutout_x_max - length/2, cutout_y_max - width/2)
    .close()
)
# Extrude the cutout sketch to create the cutout
cutout_extruded = cutout
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2296.stl