from neigbouhood.models import BussinessClass, NeigbourHood, News, Profile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
 
 
 
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_no = forms.CharField(max_length = 20)
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_no', 'password1', 'password2']



class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['neID','locationID','profile_img']


class BusinessForm(forms.ModelForm):
    class Meta:
        model=BussinessClass
        fields=['Bname','neID','Bmail','category','Bimage']

class NewsForm(forms.ModelForm):
    class Meta:
        model=News
        fields=['newsTitle','newsImage','newsDescription','location','neiba']
class NeigbahoodForm(forms.ModelForm):
    class Meta:
        model=NeigbourHood
        fields=['name','NeiLocation','occupantsCount']
