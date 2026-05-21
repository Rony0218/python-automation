"""
excel_to_summary.py
-------------------
Lee todos los archivos Excel de una carpeta, los consolida en un solo
DataFrame y genera un archivo resumen con totales y estadísticas.

Uso:
    python data_automation/excel_to_summary.py
    python data_automation/excel_to_summary.py --input "./data" --output "resumen.xlsx"
"""

import argparse
from pathlib import Path

import pandas as pd


def consolidate_excel(input_folder: Path, output_file: Path) -> None:
    files = list(input_folder.glob("*.xlsx")) + list(input_folder.glob("*.xls"))

    if not files:
        print(f"No se encontraron archivos Excel en: {input_folder}")
        return

    frames = []
    for file in files:
        print(f"  Leyendo: {file.name}")
        df = pd.read_excel(file)
        df["_archivo_origen"] = file.name
        frames.append(df)

    consolidated = pd.concat(frames, ignore_index=True)

    with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
        # Hoja 1: datos consolidados
        consolidated.to_excel(writer, sheet_name="Datos", index=False)

        # Hoja 2: resumen estadístico de columnas numéricas
        summary = consolidated.describe().T
        summary.to_excel(writer, sheet_name="Resumen")

    print(f"\nArchivo generado: {output_file}")
    print(f"  Filas totales : {len(consolidated):,}")
    print(f"  Columnas      : {list(consolidated.columns)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Consolida archivos Excel en un resumen.")
    parser.add_argument("--input",  type=str, default="./data",        help="Carpeta con archivos Excel")
    parser.add_argument("--output", type=str, default="resumen.xlsx",  help="Archivo de salida")
    args = parser.parse_args()

    consolidate_excel(Path(args.input), Path(args.output))
