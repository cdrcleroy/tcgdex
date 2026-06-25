# cards/services/tcgdex_client.py
from tcgdexsdk import TCGdex, Query

_client = None


def get_tcgdex_client():
    global _client

    if _client is None:
        _client = TCGdex("fr")

    return _client


def fetch_cards_by_name(client, name: str, page: int = 1, per_page: int = 24):
    return client.card.listSync(
        Query()
        .contains("name", name)
        .paginate(page=page, itemsPerPage=per_page)
    )
