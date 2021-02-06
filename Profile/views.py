from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import SignUpFormUser, UserLoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView,LogoutView
from django.http import HttpResponse
from django.urls import reverse
from myWeb.settings import LOGOUT_REDIRECT_URL


# Create your views here.


# This is old login view, new one is after signup view
class OldLoginView(View):

    # If get request then provide blank login form
    def get(self, request):
        return render(request, 'Profile/login.html', {'form': UserLoginForm()})

    # If post request then authenticate and log the user in and redirect him to profile page
    def post(self, request):

        # Populate the form with current values
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse('You are logged in ' + username)
            else:
                return render(request, 'Profile/login.html', {'form': form,
                                                              'errors': "Username or Password incorrect!!"})
        else:
            return render(request, 'Profile/login.html', {'form': form})


# This is SignUp view used to create users
class SignUpView(View):

    # If get request then give simple form
    def get(self, request):
        form = SignUpFormUser()
        return render(request, 'Profile/signup.html', {'form': form})

    # If post request then validate form and then store the user and create user profile
    def post(self, request):
        form = SignUpFormUser(request.POST)  # Create a form with the given input data from user
        if form.is_valid():  # If form is valid then save it else give the errors back to that page
            user = form.save()  # Save the User part of form(method inherited from UserCreation Form class)

            # Above statement will signal the UserProfile model and it will also create its object
            # Now we need to fetch it and populate it with current data received from user in POST array

            user.refresh_from_db()  # Fetch the user with its user profile created
            # Now populate the data
            # print("****************************"+form.cleaned_data['full_name']+"**************************")
            user.userprofile.full_name = form.cleaned_data['full_name']
            user.userprofile.dob = form.cleaned_data['dob']
            user.userprofile.country = form.cleaned_data['country']
            user.userprofile.lang = form.cleaned_data['lang']

            # Save the profile
            user.userprofile.save()
            # Save the user
            user.save()
            return redirect(user.userprofile.get_absolute_url())
        else:
            return render(request, 'Profile/signup.html', {'form': form})


# Currently Used Login View
class UserLoginView(LoginView):
    template_name = 'Profile/login.html'
    authentication_form = UserLoginForm
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status'] = self.kwargs['status']
        print(context)
        return context

    def form_invalid(self, form):
        return render(self.request, 'Profile/login.html', {'form': form})


# This will redirect to proper user
class RedirectToProfile(View):

    def get(self, request):
        print("****************Uid is "+str(request.user.pk)+"***************")
        return redirect(reverse("Rhythmica:profilePage"))


# This will logout a user
class Logout(LogoutView):
    next_page = LOGOUT_REDIRECT_URL

