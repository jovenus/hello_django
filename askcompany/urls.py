
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponseRedirect

def root(request):
    # TODO 차후에 reverse 기능
    return HttpResponseRedirect('/blog/')
    # return HttpResponseRedirect('http://naver.com')
    
urlpatterns = [
path('admin/', admin.site.urls),
path('blog/', include('blog.urls')),
path('shop/', include('shop.urls')),
path('', root),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
