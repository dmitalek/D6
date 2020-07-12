from django.contrib import admin
from django.conf.urls.static import static, settings
from django.urls import path, include
from p_library import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('index/', views.index),
    path('index/book_increment/', views.book_increment),
    path('index/book_decrement/', views.book_decrement),
    path('publisher/', views.Publisher),
    path('', include('p_library.urls', namespace='p_library')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
