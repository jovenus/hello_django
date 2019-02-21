from django.shortcuts import redirect, render
from .models import Shop
from .forms import ShopForm

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



def shop_new(request):
    form_cls = ShopForm

    # request.GET
    # request.POST
    # request.FILES

    if request.method == "POST":    #"GET", "POST"
            form = form_cls(request.POST, request.FILES)
            if form.is_valid():
                shop = form.save()
                return redirect('/shop/{}'.format(shop.id))
    else:
        form = form_cls()
        # form = form_cls(request.POST, request.FILES)
        # if form.is_valid():
        #     shop = form.save()
        #     return redirect('/shop/{}'.format(shop.id))

    return render(request, 'shop/shop_form.html', {
        'form':form,
    })

# Create your views here.
