"""基本体回退：检索失败时用 CadQuery 生成简单几何。"""
from pathlib import Path
from typing import Dict, Tuple

import cadquery as cq

from config import OUTPUT_DIR


def generate_primitive_stl(shape_type: str, params: Dict) -> Tuple[Path, str]:
    size = params.get("size", 10)

    if shape_type == "cube":
        result = cq.Workplane("XY").box(size, size, size)
    elif shape_type == "sphere":
        result = cq.Workplane("XY").sphere(size / 2)
    elif shape_type == "cylinder":
        result = cq.Workplane("XY").cylinder(size, size / 3)
    elif shape_type == "cone":
        r_top = max(1.0, size / 6)
        result = (
            cq.Workplane("XY")
            .circle(size / 3)
            .workplane(offset=size)
            .circle(r_top)
            .loft()
        )
    elif shape_type == "rectangle":
        w = max(5.0, min(50.0, params.get("width", size) / 10))
        h = max(5.0, min(50.0, params.get("height", size) / 10))
        result = cq.Workplane("XY").box(w, h, size / 2)
    else:
        result = cq.Workplane("XY").box(size, size, size)
        shape_type = "cube"

    stl_filename = f"{shape_type}_{int(size)}_{int(size * 100) % 100}.stl"
    stl_path = OUTPUT_DIR / stl_filename
    cq.exporters.export(result, str(stl_path))

    code = _primitive_code(shape_type, params, size)
    py_path = OUTPUT_DIR / f"generated_{shape_type}_{int(size)}.py"
    py_path.write_text(code, encoding="utf-8")

    return stl_path, shape_type


def _primitive_code(shape_type: str, params: dict, size: float) -> str:
    header = "import cadquery as cq\n\n"
    if shape_type == "cube":
        body = f"result = cq.Workplane('XY').box({size}, {size}, {size})\n"
    elif shape_type == "sphere":
        body = f"result = cq.Workplane('XY').sphere({size / 2})\n"
    elif shape_type == "cylinder":
        body = f"result = cq.Workplane('XY').cylinder({size}, {size / 3})\n"
    elif shape_type == "cone":
        r_top = max(1.0, size / 6)
        body = (
            f"result = cq.Workplane('XY').circle({size / 3})"
            f".workplane(offset={size}).circle({r_top}).loft()\n"
        )
    elif shape_type == "rectangle":
        w = max(5.0, min(50.0, params.get("width", size) / 10))
        h = max(5.0, min(50.0, params.get("height", size) / 10))
        body = f"result = cq.Workplane('XY').box({w}, {h}, {size / 2})\n"
    else:
        body = f"result = cq.Workplane('XY').box({size}, {size}, {size})\n"
    return header + body
