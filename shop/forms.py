from django import forms
from .models import Shop
# 필드 자동추가, DB로 저장 기능

class ShopForm(forms.ModelForm):        #모델폼은 자동으로 만들어지나 우리가 원하는 형태로 커스터마이징
    # title = forms.Charfield()
    # content = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Shop
        fields = '__all__'                  #모든 필드 가져오기
        # fields = ['title', 'content']     #지정 필드만 가져오기
