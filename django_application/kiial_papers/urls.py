"""
kiial_papers URL Configuration
"""
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import (
    LoginView, 
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from django.contrib import admin
from django.urls import path,include
from django_filters.views import FilterView
from papers.filters import PapersFilter


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('papers.urls', namespace="papers")),
    url(r'^search/$', FilterView.as_view(filterset_class=PapersFilter,
        template_name='papers/search.html'), name='search'),
]
