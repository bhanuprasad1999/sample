
from django.urls import path
from .views import start_coding, get_code_formater
urlpatterns = [
    path('', start_coding),
    path('get_code/', get_code_formater),
]
