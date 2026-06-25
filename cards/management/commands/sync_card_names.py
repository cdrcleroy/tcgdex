import json
import requests

from django.conf import settings
from django.core.management.base import BaseCommand

CACHE_DIR = settings.BASE_DIR / "static" / "data"
CACHE_FILE = CACHE_DIR / "card_names_fr.json"


class Command(BaseCommand):
    help = "Synchronise les noms français des Pokémon"

    def handle(self, *args, **options):
        self.stdout.write("Synchronisation des noms de Pokémon...")

        CACHE_DIR.mkdir(parents=True, exist_ok=True)

        url = "https://tyradex.app/api/v1/pokemon"

        response = requests.get(url, timeout=15)
        response.raise_for_status()

        data = response.json()

        names = []

        for pokemon in data:
            french_name = pokemon["name"]["fr"]

            if french_name == "MissingNo.":
                continue

            names.append(french_name)

        names = sorted(set(names))

        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(names, f, ensure_ascii=False, indent=2)

        self.stdout.write(f"Cache : {CACHE_FILE}")
        self.stdout.write(f"Existe : {CACHE_FILE.exists()}")
        self.stdout.write(f"{len(names)} noms récupérés")
        self.stdout.write(str(names[:10]))

        self.stdout.write(
            self.style.SUCCESS("Synchronisation terminée.")
        )
