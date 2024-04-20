from django.shortcuts import render
from acount.models import CustomerProfile

# Create your views here.
def contact(request):
    if request.method == "POST":
          listing=request.method == "GET"
    context = {
     
    }
    return render(request, 'pages/dashboard.html')
