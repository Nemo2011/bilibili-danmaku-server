from django.urls import path
 
from . import views
 
app_name = 'danmaku'

urlpatterns = [
    path("", views.index, name="homepage"),
    path("danmaku/<int:aid>/<int:page>/", views.danmaku, name="danmaku")
]
