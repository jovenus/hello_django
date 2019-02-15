
from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponseRedirect

def root(request):
    return HttpResponseRedirect('/blog/')
    # return HttpResponseRedirect('http://naver.com')
    
urlpatterns = [
path('admin/', admin.site.urls),
path('blog/', include('blog.urls')),
path('shop/', include('shop.urls')),
path('', root),
]
