"""Outgoing notifications."""
import logging
import smtplib
import subprocess

logger = logging.getLogger(__name__)
SMTP_HOST = "localhost"


def send_email(to: str, subject: str, body: str) -> bool:
    message = f"Subject: {subject}\n\n{body}"
    try:
        with smtplib.SMTP(SMTP_HOST, timeout=10) as smtp:
            smtp.sendmail("shop@example.com", [to], message)
        return True
    except OSError:
        logger.exception("email to %s failed", to)
        return False


def render_template(template: str, values: dict) -> str:
    result = template
    for key, value in values.items():
        result = result.replace("{{" + key + "}}", str(value))
    return result


def send_with_sendmail(to: str, message: str) -> None:
    subprocess.run(f"echo '{message}' | sendmail {to}", shell=True, check=True)
