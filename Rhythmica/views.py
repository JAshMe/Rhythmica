from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404,HttpResponse
from Profile.models import UserProfile
from django.views import generic
from django.views import View
from myWeb.settings import LOGIN_URL
from django.utils.html import escape,strip_tags
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Used to create the forms of create,update and delete any view
from django.urls import reverse
from .models import Album, Song, AlbumSongMap
from .forms import AddAlbumForm,AddSongForm
from django.db import IntegrityError
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


# To redirect to the home page of Rhythmica
class RedirectToRhythmica(View):

    def get(self, request):
        return redirect(reverse('Rhythmica:homePage'))


# This the home page view
class HomePage(View):

    def get(self, request):
        return render(request, 'Rhythmica/index.html')


# ----------------------------------After Logging In-----------------------------------------------

# This is profile view
class ProfileView(LoginRequiredMixin, View):

    login_url = LOGIN_URL
    # raise_exception = True
    print("********"+login_url+"********************")

    def get(self, request):
        user_pro = get_object_or_404(UserProfile, pk=request.user)
        return render(request, 'Rhythmica/profile.html', {'user_pro': user_pro})


# This class will make a view with list of certain items
# It will fetch all the items of a particular model and then pass it to the template specified
class AlbumListView(LoginRequiredMixin, generic.ListView):
    login_url = LOGIN_URL
    template_name = 'Rhythmica/album_list.html'  # This is template where the data set is to be used
    context_object_name = 'all_albums'  # To set the name of variable to be sent there

    # This is dynamic filtering of objects which need to be listed
    def get_queryset(self):  # This method is used to fetch all the elements of certain model stored in data base
        return Album.objects.filter(user=self.request.user.userprofile)  # A query set is returned which can be given to the template
    # This query set is stored in object_list by default


# This class will make a view which has detail of a particular object
# The class expects the primary key of that object passed to it by url
class DetailsView(LoginRequiredMixin, generic.DetailView):
    login_url = LOGIN_URL
    template_name = 'Rhythmica/albumDetails.html'  # The template where the value is passed
    model = Album  # The type of object which is to be detailed
    context_object_name = 'album'  # The name of object in which its to be stored
    # By default its the lower case of model name

    pk_url_kwarg = 'album_id'
    # This field is used to set name for the primary key used in url (by default its 'pk')

    extra_context = {'addSongForm': AddSongForm()}

    # There is a method which is overridden when we want to get object on our wish (or we want to do work just before
    # accessing the object), its called 'def get_object(self)' and it returns the 'object' of model we are interested

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.user != self.request.user.userprofile:
            raise Http404()
        return obj


# This class is used whenever user wants to create an album and he has to fill the form for it
# This class responds differently for different type of request ie. GET or POST
# To insert in database, it should have a POST method
class AddAlbum(LoginRequiredMixin, CreateView):
    login_url = LOGIN_URL
    #  We specify here the model to be created
    model = Album

    # Then we specify the arguments/columns of the Album filled by the user
    # This would become our fields in the form, which would be filled by the user
    template_name = 'Rhythmica/album_form.html'
    # The data is always sent to the model_form file(default), here it would be album_form
    # This can be changed by editing a variable named 'template_name_suffix'
    # This class sends the object 'form'(default name) created by itself and sends it to above mentioned file
    form_class = AddAlbumForm

    # To insert foreign key before saving, we need to override form_valid() method
    # This method is called after valid data(validation done by the form_class) has been POSTed to the form and
    # it typically saves the model and  returns http response of success_url or url to redirect after model
    # has been saved
    def form_valid(self, form):
        form.instance.user = self.request.user.userprofile
        try:
            return super().form_valid(form)
        except IntegrityError:
            return render(self.request, self.template_name, {'form': form,
                                                             'error': "This Album already exists in your collection!!",
                                                             })

    # Context Data is the data sent to the template after rendering.
    # It contains information added by the classes implicitly and we also can add data into it explicitly
    # 'context' is the associative array used for storing different values like 'variable_name'=>'variable_data'
    def get_context_data(self, **kwargs):
        context = super(AddAlbum, self).get_context_data(**kwargs)  # Getting default context from its parent class

        # Now I will add my own data to differentiate b/w Add and Update

        context['role'] = 'Add'
        return context

# For updating info of any object, we can use UpdateView for any Model


class UpdateAlbum(LoginRequiredMixin, UpdateView):
    login_url = LOGIN_URL
    model = Album
    template_name = 'Rhythmica/album_form.html'
    form_class = AddAlbumForm

    # Explanation in Above Class

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.user != self.request.user.userprofile:
            raise Http404()
        return obj

    def get_context_data(self, **kwargs):
        context = super(UpdateAlbum, self).get_context_data(**kwargs)
        context['role'] = 'Edit'
        return context


# This class will Delete the object from database whose pk is received from the URL


class DeleteAlbum(LoginRequiredMixin, DeleteView):
    login_url = LOGIN_URL
    model = Album

    # This view responds differently for different types of request
    # For GET request it will use confirmation template ('album_delete_confirm' by default)
    # and ask user to confirm it (made by programmer)
    # For POST request, it will delete the object straight away

    # If we want to implement confirmation, then we have to redirect first with 'get' to this view resulting the
    # template and then with 'post' to this view

    # No template needed right now, just delete it straightaway and redirect it to the Albums page

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.user != self.request.user.userprofile:
            raise Http404()
        return obj

    def get_success_url(self):
        return reverse('Rhythmica:albumList')


# This class will only run in backend to add songs to database and then redirect it to albumDetails page
class AddSong(LoginRequiredMixin, View):

    login_url = LOGIN_URL

    # Post request would process the data and then store it in database
    def post(self, request):

        # Populating data in our form
        album_id = request.POST['album_id']
        add_song_form = AddSongForm(request.POST, request.FILES)
        if add_song_form.is_valid():
            song = add_song_form.save(commit=False)
            song_name = song.songUrl.name.split(".")
            length = len(song_name)

            song.songTitle = song_name[0]
            for i in range(1, length-1):
                song.songTitle += "."+song_name[i]
            song.songFormat = "."+song_name[length-1]
            song.save()
            # Now linking the song with user..
            curr_album = Album.objects.get(pk=album_id)
            rel = AlbumSongMap(album=curr_album, song=song)
            rel.save()
            return HttpResponse("Song is saved!!")
        else:
            return HttpResponse("Error in saving!!")

    def get(self, request):
        return Http404()
















