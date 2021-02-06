""" 
    Author: JAshMe
    CSE, MNNIT Allahabad
 """
from . import views
from django.urls.conf import path

app_name = "Profile"

urlpatterns = [

    # accounts/login/
    path('login/<status>', views.UserLoginView.as_view(), name="loginPage"),

    # accounts/register/
    path('register/', views.SignUpView.as_view(), name="signUpPage"),

    # Redirection from Login
    path('profile/', views.RedirectToProfile.as_view(), name="redirectToProfile"),

    # Logout
    path('logout/', views.Logout.as_view(), name="logoutUser")
]