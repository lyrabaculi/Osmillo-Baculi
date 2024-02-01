from django.urls import path
from . import views
from .views import submit_donation
from .views import register
from django.conf import settings
from django.conf.urls.static import static
from .views import submit_login
from .views import save_edit

urlpatterns = [
    path ('', views.index, name="index"),
    path ('home_page', views.home_page, name="home_page"),
    path ('about_page/', views.about_page, name="about_page"),
    path ('services_page/', views.services_page, name="services_page"),
    path ('login_page/', views.login_page, name="login_page"),
    path('submit_login/', submit_login, name='submit_login'),
    path ('hair/', views.hair, name="hair"),
    path('save_edit/', save_edit, name='save_edit'),
    path('submit_donation/', submit_donation, name='submit_donation'),
    path('register/', register, name='register'),
    path ('register_page/', views.register_page, name="register_page"),
    path('delete_donation/<int:donation_id>/', views.delete_donation, name='delete_donation'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
