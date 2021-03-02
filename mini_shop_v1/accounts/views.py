from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout	
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from store.utils import cartData
from .forms import CreateUserForm, UpdateUserProfileForm



# Create your views here.

def register(request):
	if request.user.is_authenticated:
		return redirect('profile')
	
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			# pwd = form.cleaned_data.get('password')
			messages.success(request, 'Account was created for ' + user + "\nNow Log in")
			# print(user)
			# print(pwd)
			# user = authenticate(request, username=user, password=pwd)
			# print("\n", user, "\n")
			# login(request, user)
			# return redirect('profile', username = request.user.username)
			return redirect('login')
		
	context = {'form':form}
	return render(request, 'accounts/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('profile')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password) 

			if user is not None:
				login(request, user)
				return redirect('profile')
			else:
				messages.info(request, 'Username OR password is incorrect')

		return render(request, 'accounts/login.html')


def logoutUser(request):
	logout(request)
	return redirect('store')


@login_required(login_url='login')
def profile(request):
	data = cartData(request)
	cartItems = data['cartItems']

	profile = UserProfile.objects.get(user__username=request.user.username)
	print(profile.user.date_joined)
	print(profile.transations)

	context = {'profile':profile, 'cartItems':cartItems} 
	return render(request, 'profiles/detail.html', context)


def profile_update(request, *args, **kwargs):

    user = request.user
    my_profile = UserProfile.objects.get(user__username=request.user.username)
    user_data = {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "phone_number": user.phone_number,
        "bio": my_profile.bio,
        "location": my_profile.location,
    }
    form = UpdateUserProfileForm(request.POST or None, instance=my_profile, initial=user_data)
    if form.is_valid():
        profile_obj = form.save(commit=False)
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        bio = form.cleaned_data.get('bio')
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        my_profile.bio = bio
        my_profile.save()
        user.save()
        # form.save()
        profile_obj.save()
        return redirect('profile')
		
    context = {
        "form": form,
    }

    return render(request, "profiles/update.html", context)