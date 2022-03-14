from django.urls import path
from .views import (
    IndexView,
)

app_name = "papers"

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    
#    path('<int:pk>',.as_view(), name='papers-details'),
]