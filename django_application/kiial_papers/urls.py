"""
kiial_papers URL Configuration
"""
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
#from papers.views import (
#    landing_page, 
#    LandingPageView, 
#    SignupView, 
#    DashboardView
#)

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', LandingPageView.as_view(), name='landing-page'),
    
]
