from django.shortcuts import render,get_object_or_404

# view에 model(news게시글) 가져오기
from  .models import News
def main(request):
    return render(request, 'main.html')

def news(request):
    # 모든 news를 가져와 newsslist에 저장합니다.
    newslist = News.objects.all().order_by('-number')
    # news.html 페이지를 열때 모든 news인 postlist도 같이 가져옵니다.
    return render(request, 'news.html',{'newslist':newslist})

def form(request,form_id):
    news = get_object_or_404(News,pk=form_id) # newslist는 하나가 됨
    return render(request, 'news_form.html',{'news':news})
