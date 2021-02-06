""" 
    Author: JAshMe
    CSE, MNNIT Allahabad
 """

from django.urls import path, include
from . import views

app_name = 'Rhythmica'

urlpatterns = [

    # The arguments are i) the regular expression for URL and
    #  ii) the object of corresponding HttpResponse from desired function/class in views

    # For url for album details

    # /
    path('', views.HomePage.as_view(), name="homePage"),

    # accounts/
    path('accounts/', include("Profile.urls")),

    # user/2/
    path('user/', views.ProfileView.as_view(), name="profilePage"),

    # /Rhythmica/<album_id>
    path('<album_id>', views.DetailsView.as_view(), name='albumDetails'),

    # /Rhythmica/all-albums/
    path('all-albums/', views.AlbumListView.as_view(), name='albumList'),

    # /Rhythmica/albums/add/
    path('album/add/', views.AddAlbum.as_view(), name='add_album'),

    # /Rhythmica/album/2/
    path('album/<pk>/', views.UpdateAlbum.as_view(), name='upd_album'),

    # /Rhythmica/album/2/delete/
    path('album/<pk>/delete/', views.DeleteAlbum.as_view(), name='del_album'),

    # /Rhythmica/songs/add/
    path('songs/add', views.AddSong.as_view(), name='add_song'),

]
