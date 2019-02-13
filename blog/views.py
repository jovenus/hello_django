from django.http import HttpResponse
from django.shortcuts import render
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