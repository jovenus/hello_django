from django.shortcuts import render
from .models import Shop

def index(request):
    #전체 Shop 목록을 가져올 예정이다. (Lazy한 틁성)
    qs = Shop.objects.all()
    return render(request, 'shop/shop_list.html', {
        'shop_list': qs,
    })


def shop_detail(request, pk):
    # 즉시 DB로부터 데이터를 가져옵니다.
    shop = Shop.objects.get(pk=pk)
    return render(request, 'shop/shop_detail.html', {
        'shop': shop,
    })

# Create your views here.
