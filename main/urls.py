from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
	path('', views.main_view, name='main'),
    path('admin/', admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),

]
