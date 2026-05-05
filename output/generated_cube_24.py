import cadquery as cq

# 立方体
result = cq.Workplane("XY").box(24.760856204905355, 24.760856204905355, 24.760856204905355)

# 导出STL（可选）
# result.export("output.stl")
