from django.urls import path, re_path
from blog.views import index, hello_times
from blog.views import articles_by_year
from blog.views import naver_realtime_keywords
from blog.views import naver_blog_search

from django.urls import register_converter
from blog.converters import FourDigitYearConverter
from blog.converters import SlugUnicodeConverter

register_converter(FourDigitYearConverter, 'year')
register_converter(SlugUnicodeConverter, 'slug_unicode')


app_name = 'blog'  # URL Reverse 기능을 할 때, 사용.


urlpatterns = [
    path('articles/<year:year>/', articles_by_year),

    # re_path('^blog/1/$', post_detail),
    # re_path('^blog/1/edit/$', post_edit),

    path('', index),
    # re_path(r'^$', index),

    path('hello_times/<int:times>/', hello_times),
    # re_path(r'blog/hello_times/(?P<times>\d+)/$', hello_times),
    path('naver/실시간검색어/', naver_realtime_keywords),
    path('naver/네이버블로그검색/', naver_blog_search),
]
