"""Comprueba la sintaxis de los ejercicios Python sin ejecutarlos."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
PYTHON_DIR = ROOT / "Fundamentos de Programación" / "03 - Python"


def main() -> int:
    if not PYTHON_DIR.is_dir():
        print(f"No se encontró la carpeta de Python: {PYTHON_DIR}", file=sys.stderr)
        return 2

    files = sorted(PYTHON_DIR.rglob("*.py"))
    if not files:
        print("No se encontraron archivos .py para comprobar.", file=sys.stderr)
        return 2

    errors = []
    for path in files:
        try:
            source = path.read_text(encoding="utf-8-sig")
            compile(source, str(path.relative_to(ROOT)), "exec")
        except (SyntaxError, UnicodeError, OSError) as error:
            errors.append((path.relative_to(ROOT), error))

    if errors:
        print(f"Se encontraron {len(errors)} archivo(s) con problemas:")
        for path, error in errors:
            if isinstance(error, SyntaxError):
                print(f"- {path}:{error.lineno}: {error.msg}")
            else:
                print(f"- {path}: {error}")
        return 1

    print(f"Correcto: sintaxis válida en {len(files)} archivos Python.")
    print("Nota: esta comprobación no ejecuta los programas ni valida sus resultados.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
