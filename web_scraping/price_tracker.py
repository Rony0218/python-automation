"""
price_tracker.py
----------------
Extrae el precio de un producto desde una URL y guarda el historial en CSV.
Útil para monitorear precios de e-commerce a lo largo del tiempo.

Uso:
    python web_scraping/price_tracker.py --url "https://ejemplo.com/producto" --selector "span.price"
"""

import argparse
import csv
import os
from datetime import datetime

import requests
from bs4 import BeautifulSoup


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}


def fetch_price(url: str, css_selector: str) -> str | None:
    """Descarga la página y extrae el texto del primer elemento que coincida con el selector."""
    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    element = soup.select_one(css_selector)
    return element.get_text(strip=True) if element else None


def save_to_csv(output_file: str, url: str, price: str) -> None:
    file_exists = os.path.isfile(output_file)
    with open(output_file, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["fecha", "precio", "url"])
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M"), price, url])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rastrea el precio de un producto en la web.")
    parser.add_argument("--url",      required=True, help="URL del producto")
    parser.add_argument("--selector", required=True, help="Selector CSS del precio (ej: 'span.price')")
    parser.add_argument("--output",   default="precios.csv", help="Archivo CSV de salida")
    args = parser.parse_args()

    price = fetch_price(args.url, args.selector)
    if price:
        save_to_csv(args.output, args.url, price)
        print(f"Precio registrado: {price}  →  {args.output}")
    else:
        print(f"No se encontró el precio con el selector: '{args.selector}'")
