from django.urls import include, path
from . import views


app_name = 'web-notes'
urlpatterns = [
    path('', views.notesheet, name='note-sheet'),
]
