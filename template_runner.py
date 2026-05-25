"""在子进程中执行 CadQuery 模板并导出 STL。"""
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Tuple

from template_sanitize import sanitize_template_code, template_id_from_path


def prepare_export_code(code: str, template_id: str, output_stl: Path) -> str:
    import re

    code = sanitize_template_code(code, template_id)
    export_line = f'cq.exporters.export(result, r"{output_stl.as_posix()}")'
    if "cq.exporters.export" in code:
        code = re.sub(r"cq\.exporters\.export\([^)]*\)", export_line, code)
    else:
        code = code.rstrip() + "\n" + export_line + "\n"
    return code


def run_template(template_path: Path, output_stl: Path, timeout: int = 120) -> Tuple[bool, str]:
    template_id = template_id_from_path(template_path)
    code = template_path.read_text(encoding="utf-8")
    code = prepare_export_code(code, template_id, output_stl)

    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False, encoding="utf-8") as tmp:
        tmp.write(code)
        script = Path(tmp.name)

    try:
        proc = subprocess.run(
            [sys.executable, str(script)],
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=str(template_path.parent),
        )
        if proc.returncode != 0:
            err = (proc.stderr or proc.stdout or "unknown error")[:500]
            return False, err
        if not output_stl.exists():
            return False, "export finished but STL file missing"
        return True, ""
    except subprocess.TimeoutExpired:
        return False, "execution timeout"
    finally:
        script.unlink(missing_ok=True)
