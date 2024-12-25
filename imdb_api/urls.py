from django.urls import path
from imdb_api.views import *

urlpatterns=[
    # path("list/",list_view,name="movie-list"),
    # path("list/<int:pk>",detail_view,name="detail-view"),
    path("platform/",platform_list,name="platform"),
    path("platform/<int:pk>",platform_view,name="platform-view"),
    path("list/",ListView.as_view(),name="movie-list"),
    path("list/<int:pk>",ListDetail.as_view(),name="detail-view"),
]
