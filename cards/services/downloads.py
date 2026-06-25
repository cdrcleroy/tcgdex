# cards/services/downloads.py
import requests


def fetch_remote_image(image_url: str) -> bytes:
    response = requests.get(image_url, timeout=15)
    response.raise_for_status()
    return response.content
