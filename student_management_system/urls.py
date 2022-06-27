import imp
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views,hod_views,staff_views,student_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.base,name='base'),

    path('', views.doLogin,name='doLogin'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
