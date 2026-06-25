from django.urls import path

from .import views

app_name = "cards"

urlpatterns = [
    path('', views.CardSearchView.as_view(), name="cards_search"),
    path("download/", views.CardDownloadView.as_view(), name="card_download"),
]
