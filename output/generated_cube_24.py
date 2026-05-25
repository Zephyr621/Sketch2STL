import cadquery as cq

# 立方体
result = cq.Workplane("XY").box(24.18677324489565, 24.18677324489565, 24.18677324489565)

# 导出STL（可选）
# result.export("output.stl")
