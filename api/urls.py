from django.urls import path
from api.views import SearchView, search


urlpatterns = [
    path("videos/", SearchView.as_view(), name="get_videos"),
    path("search/", search, name="search")
]
