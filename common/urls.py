from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from app import views
from . import views as v


app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('', views.index, name='index'),  # '/' 에 해당되는 path
    path('logout/', v.logout_view, name='logout'),
    path('signup/', v.signup, name='signup'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# 미디어 파일 URL 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
