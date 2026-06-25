# cards/services/card_names_cache.py

from pathlib import Path
from datetime import timedelta

from django.conf import settings
from django.core.management import call_command
from django.utils import timezone


CACHE_PATH = settings.BASE_DIR / "static" / "data" / "card_names_fr.json"
MAX_AGE = timedelta(days=7)


def should_refresh_card_names_cache() -> bool:
    if not CACHE_PATH.exists():
        return True

    modified_time = timezone.datetime.fromtimestamp(
        CACHE_PATH.stat().st_mtime,
        tz=timezone.get_current_timezone(),
    )

    return timezone.now() - modified_time > MAX_AGE


def ensure_card_names_cache():
    if should_refresh_card_names_cache():
        call_command("sync_card_names")
