from django.shortcuts import redirect, render
from acount.models import *
from contact.models import Contact
from listings.models import Listing
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from acount.models import Announce
# Create your views here.
def index(request):
    announcements=Announce.objects.all()
    context = {

        "announcements":announcements,
    }
    return render(request, 'pages/index.html',context) 
  
def about(request):
    agent1=AgentProfile.objects.get(is_month_seller=True)
    agents=AgentProfile.objects.exclude(is_month_seller=True)
    context = {
        "agent_de_mois":agent1,
        "agents":agents,
    }
    return render(request, "pages/about.html",context)

def search(request):
    if request.method== "GET":
       return render(request, 'pages/search.html')
    if request.method== "POST":
        keywords=request.POST.get("keywords","")
        state=request.POST.get("state","") 
        city=request.POST.get("city","")
        price=request.POST.get("price","")
        bedrooms=request.POST.get("bedrooms","")

        search_listings=Listing.objects.filter(is_published=True)
        if keywords :
           search_listings=search_listings.filter(title__icontains=keywords)
           
        if city:
           search_listings=search_listings.filter(city__icontains=city)

        if state :
           search_listings=search_listings.filter(state__icontains=state)
        
        if bedrooms: 
            search_listings=search_listings.filter(bedrooms=bedrooms)
                
        if price: 
           search_listings=search_listings.filter(price__lte=price)
        
        context = {

        "listings":search_listings,
    }
    return render(request, "pages/search.html",context)



def register(request):
        if request.method == "POST":
            username=request.POST.get("username","")
            first_name=request.POST.get("first_name","")
            last_name=request.POST.get("last_name","")
            password=request.POST.get("password","")
            password2=request.POST.get("password2","")
            email=request.POST.get("email","")
            if User.objects.filter(username=username).exists():
                messages.error(request,"the user already exists")
                return redirect('register')
            else:
                if email and first_name and last_name  and  password and password2 :
                    if password2 == password:
                        new_user = User(           #cree objet
                            first_name=first_name,
                            last_name=last_name,
                            username=username,
                            email=email,
                            password=password,    
                        )
                        new_user.save()
                        messages.success(request,"registered succefully")
                        return redirect('login')
                    messages.error(request,"password didn't match")
                   
                else:
                    messages.error(request, "one or more fields are empty")
                    redirect("register")

        
        return render(request, 'pages/register.html')

def login(request):
    if request.method=='POST':
        username = request.POST.get("username", "")
        print(username)
        password = request.POST.get("password", "")
        print(password)
        user_authentificated = auth.authenticate(username=username,password=password)
        print(user_authentificated)
        if user_authentificated:
            auth.login(request, user_authentificated)
            return redirect("home")
        else:
            messages.error(request, "inforamtion not correct")
            return redirect("login")

    return render(request, 'pages/login.html')

def logout(request):
    if request.method == "GET":
        auth.logout(request)
        messages.success(request,"logged out")
        return redirect('home')
    return render(request, 'pages/index.html')

def dashboard(request):
    contacts=Contact.objects.filter(customer=request.user.customerprofile)
    context={
        'contacts':contacts
    }
    return render(request, 'pages/dashboard.html',context)
