from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("performers/", views.performers, name = "performers"),
    #path("performers/<str:perf_name>/", views.Perf, name = "perf"),
    path('performers/<str:perf_name>/', views.Perf, name='perf'),
    path('performers/album/<int:song_id>/', views.song, name='song'),
    path('textorder/', views.text_order, name = "textorder"),
    path('textorder/create_order', views.create_text_order, name = "createtextorder"),
]