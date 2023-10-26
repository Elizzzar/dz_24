from django.urls import path
from .views import pagination

urlpatterns = [
    path('', pagination, name='pagination')
]
