from django.shortcuts import render,redirect
from .models import Post,CODE
from . import menu


# Create your views here.
def index(request):
    return render(request,'main/index.html')
def blog(request):
    # 모든 Post를 가져와 postlist에 저장합니다
    postlist = Post.objects.all()


    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옵니다
    return render(request, 'main/blog.html', {'postlist':postlist ,'menu': menu.result('20240501')})

def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = Post.objects.get(pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'main/posting.html', {'post':post , 'menu' : menu.result('20240515')})

def new_post(request):
    if request.method == 'POST':
        if request.POST['mainphoto']:
            new_article=Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        else:
            new_article=Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        return redirect('/blog/')
    return render(request, 'main/new_post.html')


def game(request):
    return render(request,"main/game.html")



def scr(request):

    if request.method == 'CODE':
        new_article = CODE.objects.create(
            code = request.CODE['code'],
        )
    else:
        new_article = CODE.objects.create(
            code=request.CODE['code'],
        )
    return render(request,'main/scr.html',{ 'code' : code } )