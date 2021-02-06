"""
This is the views section where different webpages are listed in form of http response, which are sent when the
URL is matched in 'urls file'

The webpages are generated from the templates already stored..
So we just need to modify templates according to data and then return it
"""

from django.http import HttpResponse  # Webpages are in the HTTP Response Format
from .models import Album,Song  # To link views with database
from django.template import loader  # For loading the templates
from django.shortcuts import render, get_object_or_404  # For rendering directly without making the template variable and getting a 404 Page
from django.http import Http404  # For raising 404 Page


def index(htmlRequest):
    allAlbums = Album.objects.all()  # Retrieving all the albums from database
    template = loader.get_template('music/index.html')  # Loading the template corresponding to the index page
    context = {
        'allAlbums': allAlbums      # Giving the data to the template, so that it can be fit in it
    }

    return HttpResponse(template.render(context, htmlRequest))


def albumDetails(htmlRequest, albumId):

    # try:
    #     album = Album.objects.get(id=albumId)
    #     return render(htmlRequest, 'music/albumDetails.html', {'album': album})
    # except Album.DoesNotExist:
    #     raise Http404(htmlRequest, "Album Doesn't Exist")

    # A shorter way to do is
    album = get_object_or_404(Album, id=albumId)
    # return render(htmlRequest, 'music/albumDetails.html', {'album': album})
    return render(htmlRequest)


# this function will add the song of current album into the favorites
# and redirect back to the same page
def favorites(htmlRequest, albumId):

    album = get_object_or_404(Album, id=albumId)  # used for data passed through URL
    try:
        sel_song = Song.objects.get(id=htmlRequest.POST['favSong'])  # Accessing data from POST request
        # then selecting the song
        # if song doesn't exist then return with an error message
        sel_song.is_favorite = True
        sel_song.save()
        return render(htmlRequest, "music/albumDetails.html", {
            'album': album,
            'test': sel_song.songTitle,
        })
    except(KeyError, Song.DoesNotExist):
        return render(htmlRequest, 'music/albumDetails.html', {
            'album': album,
            'error_message': "You did not select the song properly!!",
        })






