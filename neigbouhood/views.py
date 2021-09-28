from unicodedata import category
from neigbouhood.models import BussinessClass, Category, NeigbourHood, News,Profile
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import BusinessForm, NeigbahoodForm, NewsForm, ProfileForm, UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

#################### index#######################################
@login_required(login_url='/acc/login/')
def home(request):
    categories=Category.objects.all()
    news=News.objects.filter(neiba=request.user.profile.neID)
    return render(request, 'user/index.html', {'title':'LocatEm','news':news,'categories':categories})
@login_required(login_url='/acc/login/') 
def news(request):
    news=News.objects.filter(neiba=request.user.profile.neID)
    return render(request,'home/news.html',{'news':news})
########### register here #####################################
@login_required(login_url='/acc/login/')
def biz(request,id):
    biz=BussinessClass.objects.filter(category=id,neID=request.user.profile.neID)
    for bi in biz:
        print(bi.Bimage.url)
    return render(request,'home/biz.html',{'bizness':biz})
@login_required(login_url='/acc/login/')
def update_profile(request):
    if request.method=='POST':
        profile_form=ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request,('Your profile is sucessfully updated'))
            return redirect('/')
        else:
            messages.error(request,('please correct errror below'))
    else:
        profile_form=ProfileForm(instance=request.user.profile)
    return render(request,'home/updateprofile.html',{'form':profile_form})

@login_required(login_url='/acc/login/')
def updatebiz(request,id):
    if request.method=='POST':
        b=BussinessClass.objects.get(id=id)
        profile_form=BusinessForm(request.POST,request.FILES,instance=b)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request,('Your biz is sucessfully updated'))
            return redirect('/')
        else:
            messages.error(request,('please correct errror below'))
    else:
        profile_form=BusinessForm(instance=request.user.profile)
    return render(request,'home/updatebiz.html',{'form':profile_form,'id':id})
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            ######################### mail system ####################################
            htmly = get_template('user/Email.html')
            d = { 'username': username }
            subject, from_email, to = 'welcome', 'beritamukozo@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            ##################################################################
            messages.success(request, f'Your account has been created ! You are now able to log in remember to check you mail for a welcome note !IMPORTANT YOUR LOCATION AND HOOD ARE SET FEEL FREE TO CHANGE TO WHEREVER YOU ARE')
            return redirect('Login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form, 'title':'reqister here'})
  
################ login forms###################################################
def Login(request):
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' wecome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form':form, 'title':'log in'})
@login_required(login_url='/acc/login/')
def prof(request,id):
    
    prof=User.objects.get(id=id)
    location=request.user.profile.locationID
    neibahood=request.user.profile.neID
    return render(request,'user/profile.html',{'neigbahood':neibahood,'location':location,'profile':prof})
@login_required(login_url='/acc/login/')
def search_results(request):
    if 'business' in request.GET and request.GET['business']:
        search_term=request.GET.get('business')
        searched_project=BussinessClass.search_by_title(search_term,request.user.profile.neID)
        if len(searched_project)<1:
             searched_project=NeigbourHood.find_nei(search_term)
        
        message=f"{search_term}"

        return render(request,'home/search.html',{"message":message,'search_project':searched_project})
@login_required(login_url='/acc/login/')
def create_post(request):
        form=BusinessForm()
    # if not request.user.is_staff==1:
    #     messages.info('No you are not an admin in this place')
    #     return redirect('/')
    # else:
        if request.POST:
            form=BusinessForm(request.POST,request.FILES)
            user=User.objects.get(id=request.user.id)
           
            post=form.save(commit=False)
            post.owner=user
            post.save()

            # form.save(Bname=request.data.get('name'),neID=neiba,Bmail=request.data.get('Email'),category=cat,owner=user)
            print('form')
            return redirect('/')
        else:
            form=BusinessForm()
        return render(request,'home/createform.html',{'form':form})
@login_required(login_url='/acc/login/')
def create_news(request):
        form=NewsForm()
    # if not request.user.is_staff==1:
    #     # messages.info('No you are not an admin in this place')
    #     return redirect('/')
    # else:
        if request.POST:
            form=NewsForm(request.POST,request.FILES)
            user=User.objects.get(id=request.user.id)
           
           
            post=form.save(commit=False)
            post.writer=user
            post.save()

            # form.save(Bname=request.data.get('name'),neID=neiba,Bmail=request.data.get('Email'),category=cat,owner=user)
            print('form')
            return redirect('/')
        else:
            form=NewsForm()
        return render(request,'home/createnewsform.html',{'form':form})
@login_required(login_url='/acc/login/')
def create_neiba(request):
        form=NeigbahoodForm()
   
        if request.POST:
            form=NeigbahoodForm(request.POST)
            user=User.objects.get(id=request.user.id)
           
            post=form.save(commit=False)
            post.admin=user
            post.users=user
            post.save()

            # form.save(Bname=request.data.get('name'),neID=neiba,Bmail=request.data.get('Email'),category=cat,owner=user)
            print('form')
            return redirect('/')
        else:
            form=NeigbahoodForm()
        return render(request,'home/createNeibahood.html',{'form':form})

@login_required(login_url='/acc/login/')
def delHood(request,name):
    pds=request.user.profile.neID
    
    p=NeigbourHood.objects.get(name=pds)
    post=NeigbourHood.objects.get(name=name)
    if not p.id==post.id:

        post.delete()
        return redirect('/')
    else:
        print('you in this location')
        messages.add_message(request, messages.INFO, 'Sorry you cant delete current Hood')
        return redirect('neibaHood')
@login_required(login_url='/acc/login/')
def deletebiz(request,id):
  
    post=BussinessClass.objects.get(id=id)
    if not post.owner==request.user.id:

        post.delete()
        return redirect('/')
    else:
        
        messages.add_message(request, messages.INFO, 'Sorry you cant delete current it does not belong to you')
        return redirect('/')
@login_required(login_url='/acc/login/')
def neibas(request):
    neibas=NeigbourHood.objects.all()
    return render(request,'home/neibas.html',{'neibas':neibas})
@login_required(login_url='/acc/login/')
def users(request):
    users=Profile.objects.filter(neID=request.user.profile.neID)
    return render(request,'home/users.html',{'user':users})
@login_required(login_url='/acc/login/')
def update_Neibas(request,id):
     if 'namel' in request.GET and request.GET['namel']:
        update_term=request.GET.get('namel')
        NeigbourHood.objects.filter(id=id).update(name=update_term)

        
        return redirect('/')
     return render(request,'home/updateHood.html',{'id':id,'name':id})

@login_required(login_url='/acc/login/')
def update_Occupants(request,id):
     if 'namel' in request.GET and request.GET['namel']:
        update_term=request.GET.get('namel')
        NeigbourHood.objects.filter(id=id).update(occupantsCount=update_term)

        
        return redirect('neibaHood')
     return render(request,'home/updateOccupants.html',{'id':id,'name':id})


