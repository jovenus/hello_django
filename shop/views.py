from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Shop
from .forms import ShopForm

# def index(request):
#     #전체 Shop 목록을 가져올 예정이다. (Lazy한 틁성)
#     qs = Shop.objects.all()
#     return render(request, 'shop/shop_list.html', {
#         'shop_list': qs,
#     })

class PostListView(ListView):
    model = Shop

    def get_context_data(self):
        context = super().get_context_data()
        context.update({
            'hello': 'world',
        })
        return context

index = PostListView.as_view()

# def shop_detail(request, pk):
#     # 즉시 DB로부터 데이터를 가져옵니다.
#     shop = Shop.objects.get(pk=pk)
#     return render(request, 'shop/shop_detail.html', {
#         'shop': shop,
#     })

shop_detail = DetailView.as_view(model=Shop)

def shop_new(request):
    form_cls = ShopForm

    # request.GET
    # request.POST
    # request.FILES

    if request.method == "POST":    #"GET", "POST"
            form = form_cls(request.POST, request.FILES)
            if form.is_valid():
                shop = form.save()
                return redirect(shop)
    else:
        form = form_cls()
        # form = form_cls(request.POST, request.FILES)
        # if form.is_valid():
        #     shop = form.save()
        #     return redirect('/shop/{}'.format(shop.id))

    return render(request, 'shop/shop_form.html', {
        'form':form,
    })

# from django.views.generic import CreateView

shop_new_cbv = CreateView.as_view(
    model=Shop, form_class=ShopForm)

def shop_edit(request, pk):
    # try:
    #   shop = Shop.objects.get(pk=pk)
    # except Shop.DoesNotExists:
    #     raise Http404   #django.http.http404

    shop = get_object_or_404(Shop, pk=pk)  #위 내용을 한줄로 표현

    form_cls = ShopForm

    if request.method == "POST":    #"GET", "POST"
            form = form_cls(request.POST, request.FILES, instance=shop)
            if form.is_valid():
                shop = form.save()
                return redirect(shop)
    else:
        form = form_cls(instance=shop)

    return render(request, 'shop/shop_form.html', {
        'form':form,
    })

# from django.views.generic import UpdateView

shop_edit_cbv = UpdateView.as_view(
    model=Shop, form_class=ShopForm)

def shop_del(request, pk):
    shop = get_object_or_404(Shop, pk=pk)

    if request.method == 'POST':
        shop.delete()
        return redirect('shop:index')


    return render(request, 'shop/shop_confirm_delete.html', {
        'shop': shop,
    })


# Create your views here.
