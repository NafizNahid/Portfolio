from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings 
from django.conf.urls.static import static
from django.views.static import serve


urlpatterns = [
    path('', include('main.urls')),
    path("admin/", admin.site.urls),
    path('main/', include('main.urls')),
    
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)