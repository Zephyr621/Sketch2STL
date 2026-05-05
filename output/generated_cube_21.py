import cadquery as cq

# 立方体
result = cq.Workplane("XY").box(21.87007087322764, 21.87007087322764, 21.87007087322764)

# 导出STL（可选）
# result.export("output.stl")
