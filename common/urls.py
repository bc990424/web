from django.urls import path
from django.contrib.auth import views as auth_views
from common.views import login
from django.conf.urls.static import static
from django.conf import settings

app_name = 'common'

urlpatterns = [
    path('login/', login, name='login'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# 미디어 파일 URL 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)