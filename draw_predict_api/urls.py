from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('draw_predict.urls')),
    path('class', include('draw_predict.urls')),
    path('draw-predict', include('draw_predict.urls')),
    # path('draw-predict', include('draw_predict.urls')),
    path('admin/', admin.site.urls),
]