from django.contrib import admin
from django.urls import path

import pumaguaAPP.views as views

app_name = "pumaguaAPP"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='Home'),
    path('informes/', views.informes, name='info')
]
