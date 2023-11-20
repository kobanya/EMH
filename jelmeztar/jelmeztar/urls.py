from django.urls import path
from django.contrib import admin

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name='index.html'), name='index'),

]


