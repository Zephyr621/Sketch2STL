"""修复 data/fixed_code 中常见的 CadQuery 模板语法问题。"""
import ast
import re
from pathlib import Path
from typing import Optional, Tuple


def template_id_from_path(path: Path) -> str:
    name = path.stem
    if name.startswith("exec_"):
        return name[5:]
    return name


def infer_result_variable(code: str) -> str:
    if re.search(r"\bassembly\s*=", code):
        return "assembly"
    parts = re.findall(r"\b(part_\d+)\s*=", code)
    if parts:
        return parts[-1]
    return "part_1"


def sanitize_template_code(code: str, template_id: str) -> str:
    code = code.replace("\r\n", "\n")

    code = re.sub(r"cq\.cq\.exporters", "cq.exporters", code)
    code = re.sub(r"cq\.cq\.", "cq.", code)
    code = re.sub(r"\{result_var\}", "result", code)

    # 去掉残缺的 exporters. / cq. 单行
    code = re.sub(r"^exporters\.\s*$", "", code, flags=re.MULTILINE)
    code = re.sub(r"^cq\.\s*$", "", code, flags=re.MULTILINE)
    code = re.sub(r"^cq\.exp\s*$", "", code, flags=re.MULTILINE)

    # 未闭合的 export 字符串
    code = re.sub(
        r'cq\.exporters\.export\(\s*result\s*,\s*"output_\d+\.stl\s*$',
        f'cq.exporters.export(result, "output_{template_id}.stl")',
        code,
        flags=re.MULTILINE,
    )
    code = re.sub(
        r'cq\.exporters\.export\(\s*(\w+)\s*,\s*"([^"]*)\.stl([^")]*)\s*$',
        r'cq.exporters.export(\1, "\2.stl")',
        code,
        flags=re.MULTILINE,
    )

    # 重复粘连的文件名 output_1264.stl"output_1264.stl
    code = re.sub(
        r'"output_(\d+)\.stl"output_\1\.stl',
        r'"output_\1.stl"',
        code,
    )

    if re.search(r"^\s*result\s*=\s*result\s*$", code, re.MULTILINE):
        var = infer_result_variable(code)
        code = re.sub(r"^\s*result\s*=\s*result\s*$", f"result = {var}", code, flags=re.MULTILINE)

    if "result =" not in code and "import cadquery" in code:
        var = infer_result_variable(code)
        code = code.rstrip() + f"\n\nresult = {var}\n"

    if "cq.exporters.export" not in code:
        code = code.rstrip() + f'\n\ncq.exporters.export(result, "output_{template_id}.stl")\n'

    return code


def check_syntax(code: str) -> Tuple[bool, Optional[str]]:
    try:
        ast.parse(code)
        return True, None
    except SyntaxError as e:
        return False, str(e)
