from django.http import HttpResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def articles_by_year(request, year):
    return HttpResponse(f'''
        {year}년도에 대한 목록
    ''')
    
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