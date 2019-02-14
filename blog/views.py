from django.http import HttpResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def articles_by_year(request, year):
    return HttpResponse(f'''
        {year}년도에 대한 목록
    ''')

 # def fn(template_name):
#     def inner(request):
#         return render(request, template_name)
#     return inner

 # index = fn('blog/index.html')

 # index2 = fn('blog/index2.html')


 # class MyTemplateView:
#     @classmethod
#     def as_view(self, template_name):
#         def inner(request):
#             return render(request, template_name)
#         return inner

 # index = MyTemplateView.as_view('blog/index.html')


    from django.views.generic import TemplateView

    index = TemplateView.as_view(template_name='blog/index.html')


def hello_times(request, times):
    message = "안녕하세요"*times
    return HttpResponse(message)

def naver_realtime_keywords(request):
    res = requests.get("http://naver.com")
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    tag_list = soup.select('.PM_CL_realtimeKeyword_rolling .ah_k')
    text = '<br/>\n'.join([tag.text for tag in tag_list])
    return HttpResponse(text)

def naver_blog_search(request):
    query = request.GET.get('query', '')  # Key가 없으면 None을 반환
    post_list = []# Key가 없으면 None을 반환
    
    if query:
        # text = f'{query} 검색할꺼야.'
        url = 'https://search.naver.com/search.naver'
        params = {
            'where': 'post',
            'sm': 'tab_jum',
            'query': query,
        }
        res = requests.get(url, params=params)
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')
        tag_list = soup.select('.sh_blog_title')
        # post_list = []
        for tag in tag_list:
            post_url = tag['href']
            post_title = tag['title']
            post_list.append({
                'title': post_title,
                'url': post_url,
            })
        # blog/templates/blog/naver_blog_search.html
    return render(request, 'blog/naver_blog_search.html', {
        'query': query,
        'post_list': post_list,
    })
    # else:
    #     text = '검색어를 지정해주세요.'
    # return HttpResponse(text)

def 사원증_이미지_응답(request):
    # ttf_path = 'C:/Windows/Fonts/malgun.ttf' # 윈도우, 맥:
    ttf_path = 'assets/fonts/malgun.ttf'
    # ttf_path = '/Library/Fonts/AppleGothic.ttf'

     # FIXME: 각 운영체제에 맞게 경로를 설정해주세요.
    # 파일을 복사한 후에, 경로 확인 후에 적용해주세요.
    # ttf_path = 'assets/fonts/AppleGothic.ttf'

    text = request.GET.get('name', '익명')
    # text = '이진석 (사번: 201900001)'

    image_url = 'http://www.flowermeaning.com/flower-pics/Calla-Lily-Meaning.jpg'
    res = requests.get(image_url) # 서버로 HTTP GET 요청하여, 응답 획득

    io = BytesIO(res.content) # 응답의 Raw Body  메모리 파일 객체 BytesIO 인스턴스 생성
    io.seek(0) # 파일의 처음으로 커서를 이동
    canvas = Image.open(io).convert('RGBA') # 이미지 파일을 열고, RGBA 모드로 변환
    font = ImageFont.truetype(ttf_path, 40) # 지정 경로의 TrueType 폰트, 폰트크기 40
    draw = ImageDraw.Draw(canvas) # canvas에 대한 ImageDraw 객체 획득

    left, top = 10, 10
    margin = 10
    width, height = font.getsize(text)
    right = left + width + margin
    bottom = top + height + margin

    draw.rectangle((left, top, right, bottom), (255, 255, 224))
    draw.text((15,15), text, font=font, fill=(20, 20, 20))

     # canvas.show()  # 뷰에서는 필요가 없어서, 주석처리

    response = HttpResponse(content_type='image/png')
    canvas.save(response, format='PNG')    # HttpResponse 의 file-like 특성 활용
    return response