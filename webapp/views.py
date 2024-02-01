from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import DonationForm
from .models import Donation
from .forms import RegistrationForm
from .models import UserAccount
from django.contrib.auth import authenticate, login
from.forms import LoginForm
from django.utils.text import normalize_newlines
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


def index(request):
    return render(request, 'pages/index.html')

def home_page(request):
    return render(request, 'pages/home.html')

def about_page(request):
    return render(request, 'pages/about.html')

def services_page(request):
    return render(request, 'pages/services.html')



from django.utils.text import normalize_newlines

def submit_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password1')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('home_page')
        else:
            messages.error(request, 'Invalid login credentials')
    else:
        # Handle GET requests or other cases
        pass

    return render(request, 'pages/login.html')




def register_page(request):
    return render(request, 'pages/register_page.html')

def login_page(request):
    return render(request, 'pages/login.html')
def submit_donation(request):
    if request.method == 'POST':
        form = DonationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your donation!')
            return redirect('services_page')
    else:
        form = DonationForm()

    return render(request, 'services_page.html', {'form': form})

def hair(request):
    return render(request, 'pages/hair.html')


def hair(request):
    donations = Donation.objects.all()
    return render(request, 'pages/hair.html', {'donations': donations})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('register_page')
    else:
        form = RegistrationForm()

    return render(request, 'pages/register_page.html', {'form': form})




def save_edit(request):
    if request.method == 'POST':
        donation_id = request.POST.get('editDonationId')
        if donation_id:
            try:
                donation = get_object_or_404(Donation, pk=donation_id)
                donation.full_name = request.POST.get('editFullName')
                donation.age = request.POST.get('editAge')
                donation.gender = request.POST.get('editGender')
                donation.phone_number = request.POST.get('editPhoneNumber')
                donation.address = request.POST.get('editAddress')
                donation.save()
                messages.success(request, 'The donation details have been successfully updated')
                return redirect('hair')
            except Exception as e:
                return JsonResponse({'success': False, 'error': str(e)})
        else:
            return JsonResponse({'success': False, 'error': 'No donation ID provided'})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})

def delete_donation(request, donation_id):
    if request.method == 'POST':
        donation = get_object_or_404(Donation, pk=donation_id)
        donation.delete()
        messages.success(request, 'Donation successfully deleted.')
        return JsonResponse({'success': True, 'message': 'Donation successfully deleted.'})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})








