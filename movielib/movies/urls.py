from django.urls import URLPattern, path

from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('library/', views.library, name='library')
]