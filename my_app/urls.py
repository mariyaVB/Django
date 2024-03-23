from django.urls import path, re_path
import my_app.views as art

urlpatterns = [
    path('', art.info_main),
    path('<slug:painting_slug>/', art.info_art),
]
