"""
organize_files.py
-----------------
Organiza todos los archivos de una carpeta en subcarpetas por extensión.

Uso:
    python file_automation/organize_files.py
    python file_automation/organize_files.py --folder "C:/Users/TuUsuario/Downloads"
"""

import argparse
import shutil
from pathlib import Path

EXTENSION_MAP = {
    "Imagenes":   {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"},
    "Documentos": {".pdf", ".docx", ".doc", ".txt", ".pptx", ".ppt"},
    "Excel":      {".xlsx", ".xls", ".csv"},
    "Videos":     {".mp4", ".mov", ".avi", ".mkv"},
    "Audio":      {".mp3", ".wav", ".flac", ".aac"},
    "Codigo":     {".py", ".js", ".ts", ".html", ".css", ".json", ".sql"},
    "Comprimidos":{".zip", ".rar", ".7z", ".tar", ".gz"},
    "Otros":      set(),
}


def get_category(extension: str) -> str:
    for category, extensions in EXTENSION_MAP.items():
        if extension.lower() in extensions:
            return category
    return "Otros"


def organize(folder: Path) -> None:
    if not folder.exists():
        print(f"La carpeta no existe: {folder}")
        return

    moved = 0
    for file in folder.iterdir():
        if not file.is_file():
            continue

        category = get_category(file.suffix)
        dest_folder = folder / category
        dest_folder.mkdir(exist_ok=True)

        dest = dest_folder / file.name
        # Evitar sobrescribir: agrega sufijo numérico si ya existe
        counter = 1
        while dest.exists():
            dest = dest_folder / f"{file.stem}_{counter}{file.suffix}"
            counter += 1

        shutil.move(str(file), str(dest))
        print(f"  {file.name}  →  {category}/")
        moved += 1

    print(f"\nListo. {moved} archivo(s) organizados en '{folder}'.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Organiza archivos por tipo en subcarpetas.")
    parser.add_argument(
        "--folder",
        type=str,
        default=str(Path.home() / "Downloads"),
        help="Carpeta a organizar (por defecto: ~/Downloads)",
    )
    args = parser.parse_args()
    organize(Path(args.folder))
