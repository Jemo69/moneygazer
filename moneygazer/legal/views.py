from django.shortcuts import render
from .models import User

# Create your views here.
def terms(request):
    return render(request,'legal/toc.html')
def privacy(request):
    return render(request,'legal/privacy.html')
def home(request):
        if request.method == 'POST':
            user_name = request.POST.get('user_name')
            user_email = request.POST.get('user_email')
        
        # Process the data (e.g., save to database, send email, etc.)
        # For example, you could print it to the console
            new_user = User(name=user_name, email=user_email)
            new_user.save() 
        
    # Redirect after processing
       
        return render(request,'legal/home.html')
        


def price(request):
        return render(request,'legal/pricing.html',)