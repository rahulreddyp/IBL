from django.shortcuts import render, redirect, HttpResponse
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Signup, Business
from django.contrib.auth.models import User
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            messages.success(request, f'Account Created for {username}!')
            # name = request.POST.get('name')
            email = form.cleaned_data.get('email')
            mno = form.cleaned_data.get('MobileNo')
            pwd = form.cleaned_data.get('password1')
            # pwd = pbkdf2_sha256.hash("request.POST.get('pwd')")
            post = Signup(user=user, ap_email=email, ap_mob=mno, ap_ip_addr="127.0.0.1", ap_pass=pwd)
            post.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def home(request):
    if request.method == "POST" and "apply" in request.POST:
        return render(request, 'ApplyLoan/bdetails.html', {})
    else:
        return render(request, 'home.html', {})

def busdetails(request):
    if request.method == "POST":
        details = Business()
        details.b_name = request.POST.get('b_name')
        details.b_owner_name = request.POST.get('b_owner_name')
        details.b_contact = request.POST.get('b_contact')
        details.b_addr = request.POST.get('b_addr')
        details.b_pan_no = request.POST.get('b_pan_no')
        details.b_est_date = request.POST.get('b_est_date')
        details.b_type = request.POST.get('b_type')
        details.save()
        return HttpResponse("Details saved")
    else:
        return render(request, 'ApplyLoan/bdetails.html')
