"""askcompany URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog.views import index, hello_times

urlpatterns = [
    # re_path('^blog/1/$', post detail),
    # re_path('^blog/1/edit/$', post_edit)
    path('admin/', admin.site.urls),
    path('blog/hello_times/<int:times>/', hello_times),
    # re_path(r'blog/hello_times/(?P<times>\d+)/$', hello_times),
    path('', index),
    # re_path('^$', index)
]
