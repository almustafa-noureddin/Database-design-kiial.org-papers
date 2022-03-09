from django.urls import path
from .views import (
    PapersListView,
)

app_name = "papers"

#urlpatterns = [
#    path('', .as_view(), name='papers-list'),
#    path('<int:pk>',.as_view(), name='papers-details'),
#]