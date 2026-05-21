<div align="center">

  <img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:3776AB,100:0d1117&height=140&section=header&text=Python%20Automation&fontSize=36&fontColor=ffffff&fontAlignY=38&desc=Scripts%20de%20automatizacion%20para%20el%20dia%20a%20dia&descAlignY=60&descSize=16" />

  ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
  ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
  ![OpenPyXL](https://img.shields.io/badge/OpenPyXL-107C41?style=for-the-badge&logo=microsoftexcel&logoColor=white)
  ![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

</div>

## 📂 Estructura del Repositorio

```
python-automation/
│
├── 📧 email_automation/       → Envío automático de correos y reportes
├── 📁 file_automation/        → Organización y gestión de archivos
├── 📊 data_automation/        → Procesamiento de Excel, CSV y datos
└── 🌐 web_scraping/           → Extracción de datos desde la web
```

---

## 📧 Email Automation

### `send_report.py`
Envía correos automáticos con archivos adjuntos (reportes, Excel, PDFs) usando Gmail.

```bash
python email_automation/send_report.py
```

---

## 📁 File Automation

### `organize_files.py`
Organiza automáticamente los archivos de una carpeta en subcarpetas por extensión (`.xlsx`, `.pdf`, `.png`, etc.).

```bash
python file_automation/organize_files.py --folder "C:/Users/TuUsuario/Downloads"
```

---

## 📊 Data Automation

### `excel_to_summary.py`
Lee múltiples archivos Excel de una carpeta, los consolida y genera un reporte resumen con totales y estadísticas.

```bash
python data_automation/excel_to_summary.py --input "./data" --output "resumen.xlsx"
```

---

## 🌐 Web Scraping

### `price_tracker.py`
Extrae precios de un sitio web y guarda el historial en un CSV para análisis posterior.

```bash
python web_scraping/price_tracker.py --url "https://ejemplo.com" --output "precios.csv"
```

---

## ⚙️ Instalación

```bash
# Clonar el repositorio
git clone https://github.com/Rony0218/python-automation.git
cd python-automation

# Instalar dependencias
pip install -r requirements.txt
```

---

## 🧰 Requisitos

| Librería | Uso |
|---|---|
| `pandas` | Manipulación de datos |
| `openpyxl` | Lectura/escritura de Excel |
| `smtplib` | Envío de correos (incluido en Python) |
| `requests` | Peticiones HTTP |
| `beautifulsoup4` | Parsing de HTML |

---

<div align="center">
  <img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:3776AB,100:0d1117&height=100&section=footer" />
  <sub>by <a href="https://github.com/Rony0218">@Rony0218</a> · <a href="https://ronyguerrero.com">ronyguerrero.com</a></sub>
</div>
