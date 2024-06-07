from django.contrib import admin
from django.urls import path
from app.views import index, blog, posting, new_post, scr, game
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # 웹사이트 첫화면은 index 페이지
    path('blog/', blog, name='blog'),  # 블로그 리스트 페이지
    path('blog/<int:pk>/', posting, name='posting'),  # 게시글 세부 페이지
    path('blog/new_post/', new_post, name='new_post'),  # 새로운 게시글 작성 페이지
    path('blog/scr/', scr, name='scr'),  # 'scr' 이름의 커스텀 뷰
    path('game/', game, name='game'),  # 게임 페이지
]

# 정적 파일 URL 설정
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# 미디어 파일 URL 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
