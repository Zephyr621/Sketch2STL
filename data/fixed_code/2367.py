import cadquery as cq
from cadquery import exporters
# --- Part 1: Rectangular Plate ---
part_1_length = 0.4871 * 0.4871  # Scaled length
part_1_width = 0.3103 * 0.4871   # Scaled width
part_1_height = 0.0296
cutout_x_start = 0.0808 * 0.4871
cutout_y_start = 0.0426 * 0.4871
cutout_width = (0.4146 - 0.0808) * 0.4871
cutout_height = (0.2776 - 0.0426) * 0.4871
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
    .faces(">Z").workplane()
    .moveTo(cutout_x_start - part_1_length/2, cutout_y_start - part_1_width/2)
    .rect(cutout_width, cutout_height)
    .cutThruAll()
)
# --- Part 2: Cutout ---
part_2_length = 0.481 * 0.481  # Scaled length
part_2_width = 0.2801 * 0.481   # Scaled width
part_2_height = 0.02
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2367.stl