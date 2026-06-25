# cards/services/cards.py
from .tcgdex_client import get_tcgdex_client, fetch_cards_by_name


def get_cards(name: str, page: int = 1, per_page: int = 24) -> dict:
    client = get_tcgdex_client()
    raw_cards = fetch_cards_by_name(client, name, page, per_page)

    cards = []

    for raw_card in raw_cards:
        image_url = raw_card.get_image_url(
            quality="high",
            extension="png",
        )

        if not image_url:
            continue

        image_light = raw_card.get_image_url(
            quality="low",
            extension="webp",
        )

        cards.append({
            "id": raw_card.id,
            "name": raw_card.name,
            "image_url": image_url,
            "image_light": image_light,
            "download_name": f"{raw_card.name}-{raw_card.id}",
        })

    return {
        "cards": cards,
        "page": page,
        "per_page": per_page,
        "has_previous": page > 1,
        "has_next": len(raw_cards) == per_page,
        "previous_page": page - 1,
        "next_page": page + 1,
    }
