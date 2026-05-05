# -*- coding: utf-8 -*-
import sys
import os

# 设置工作目录
os.chdir(r"D:\自然语言处理\cad query环境\all_stl_files")

# 打印环境信息
print(f"Python: {sys.executable}")
print(f"工作目录: {os.getcwd()}")

# 导入cadquery
try:
    import cadquery as cq
    print(f"CadQuery版本: {cq.__version__}")
except ImportError as e:
    print(f"导入失败: {e}")
    print("系统路径:")
    for p in sys.path[:5]:
        print(f"  {p}")
    sys.exit(1)

# 执行修复后的代码
import cadquery as cq
from math import radians

# --- Part 1: Rectangular Prism ---
part_1_length = 0.1489 * 0.1489  # Scaled length
part_1_width = 0.0718 * 0.1489   # Scaled width
part_1_height = 0.0431

part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)

# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0.0234, 0.75, 0))

# --- Part 2: Rectangular Protrusion ---
part_2_length = 0.1489 * 0.1489  # Scaled length
part_2_width = 0.0254 * 0.1489   # Scaled width
part_2_height = 0.001
# 创建part_2
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_length, part_2_width)
    .extrude(part_2_height)
)

# Export


# 定义结果变量
result = part_1

# 导出为STL文件
cq.exporters.export(result, "output_0.stl")
