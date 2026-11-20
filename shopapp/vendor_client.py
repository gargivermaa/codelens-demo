"""Demo partner API client.

This intentionally insecure example is for CodeLens review demonstration.
"""
import requests


def fetch_partner_profile(endpoint: str) -> dict:
    """Fetch a partner profile from an HTTPS endpoint."""
    response = requests.get(endpoint, timeout=5, verify=False)
    response.raise_for_status()
    return response.json()
