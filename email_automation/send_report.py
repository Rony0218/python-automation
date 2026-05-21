"""
send_report.py
--------------
Envía un correo automático con un archivo adjunto usando Gmail.

Configuración:
  - Crea un archivo .env en la raíz del proyecto con:
      EMAIL_USER=tucorreo@gmail.com
      EMAIL_PASS=tu_app_password  (no tu contraseña normal, genera una en: myaccount.google.com/apppasswords)
"""

import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def send_email(
    to: str,
    subject: str,
    body: str,
    attachment_path: str | None = None,
    sender: str | None = None,
    password: str | None = None,
):
    """
    Envía un correo electrónico con o sin adjunto.

    Args:
        to: Destinatario (o lista separada por comas).
        subject: Asunto del correo.
        body: Cuerpo del mensaje (HTML permitido).
        attachment_path: Ruta al archivo adjunto (opcional).
        sender: Correo remitente. Si es None, lee EMAIL_USER del entorno.
        password: Contraseña de app. Si es None, lee EMAIL_PASS del entorno.
    """
    sender = sender or os.environ.get("EMAIL_USER")
    password = password or os.environ.get("EMAIL_PASS")

    if not sender or not password:
        raise ValueError(
            "Define EMAIL_USER y EMAIL_PASS como variables de entorno o pásalos como parámetros."
        )

    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = to
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "html"))

    if attachment_path:
        with open(attachment_path, "rb") as f:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(f.read())
        encoders.encode_base64(part)
        filename = os.path.basename(attachment_path)
        part.add_header("Content-Disposition", f"attachment; filename={filename}")
        msg.attach(part)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.sendmail(sender, to.split(","), msg.as_string())

    print(f"Correo enviado exitosamente a: {to}")


if __name__ == "__main__":
    # --- Ejemplo de uso ---
    send_email(
        to="destinatario@ejemplo.com",
        subject="Reporte Semanal 📊",
        body="<h2>Hola,</h2><p>Adjunto el reporte de esta semana.</p>",
        attachment_path="reporte.xlsx",  # Cambia por tu archivo
    )
