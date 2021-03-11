from django.urls import path, include
from django.contrib import admin

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('simpleblog.urls')),
	path ('users/', include('django.contrib.auth.urls')),
	path('users/', include('users.urls')),

]
