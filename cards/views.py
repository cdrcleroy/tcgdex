# views.py
from django.http import HttpResponse
from django.utils.text import slugify
from django.views.generic import View, FormView

from .forms import CardSearchForm
from cards.services.cards import get_cards
from cards.services.downloads import fetch_remote_image
from cards.services.card_names_cache import ensure_card_names_cache


class CardSearchView(FormView):
    template_name = "cards/card_search.html"
    form_class = CardSearchForm

    def dispatch(self, request, *args, **kwargs):
        ensure_card_names_cache()
        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        initial = super().get_initial()
        initial["name"] = self.request.GET.get("name", "")
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        name = self.request.GET.get("name")
        page = int(self.request.GET.get("page", 1))

        if name:
            result = get_cards(name=name, page=page, per_page=24)

            context["cards"] = result["cards"]
            context["search"] = name
            context["pagination"] = result

        return context

    def form_valid(self, form):
        name = form.cleaned_data["name"]

        return self.redirect_to_search(name)

    def redirect_to_search(self, name):
        from django.shortcuts import redirect
        from django.urls import reverse
        from urllib.parse import urlencode

        url = reverse("cards:cards_search")
        querystring = urlencode({
            "name": name,
            "page": 1,
        })

        return redirect(f"{url}?{querystring}")


class CardDownloadView(View):
    def get(self, request, *args, **kwargs):
        image_url = request.GET.get("url")
        name = request.GET.get("name", "pokemon-card")

        if not image_url or image_url == "None":
            return HttpResponse("URL manquante", status=400)

        image_content = fetch_remote_image(image_url)

        filename = f"{slugify(name)}.png"

        response = HttpResponse(
            image_content,
            content_type="image/png",
        )
        response["Content-Disposition"] = f'attachment; filename="{filename}"'

        return response
