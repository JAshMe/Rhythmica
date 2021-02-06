"""
Author: JAshMe
CSE, MNNIT Allahabad
"""

from django.db import models
from Profile.models import UserProfile
from django.urls import reverse
from myWeb import settings
from django.core.files.storage import FileSystemStorage

# These models are used to model the code as well as the database
# The classes we make can be actually the tables in database and its instance variable scan be made its columns
# with different objects as its rows


class Song(models.Model):
    # Each song must be independent to user, because same users can share a song
    songTitle = models.CharField(max_length=500, verbose_name="Song Title")
    songFormat = models.CharField(max_length=10, verbose_name="Format")
    songDuration = models.TimeField(verbose_name="Duration", blank=True, null=True)
    songUrl = models.FileField(verbose_name="Choose Song", upload_to='songs')
    songLogo = models.ImageField(verbose_name="Choose Logo", upload_to='song_logos',
                                 default='/song_logos/anonymous.jpg', null=True)

    def __str__(self):
        return self.songTitle


class Album(models.Model):
    artist = models.CharField(max_length=250, verbose_name='Album Artist')
    albumTitle = models.CharField(max_length=1000, verbose_name='Album Title')
    numOfSongs = models.IntegerField(verbose_name='Number of Songs', default=0, null=True)
    genre = models.CharField(max_length=50, verbose_name='Album Genre', blank=True, default='Unknown')

    # albumLogo will be stored as file on server(may be different from current one)
    is_private = models.BooleanField(verbose_name="Is Private", default=False)

    albumLogo = models.ImageField(verbose_name='Album Logo', upload_to='album_logos',
                                  default='/song_logos/anonymous.jpg', blank=True)
    # File Field for logo image

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    songs = models.ManyToManyField(Song, verbose_name="Songs", through="AlbumSongMap")
    # Creating many to many fields for Song through the relationship defined in Album_Song_Map

    # Other than this it, will also make a primary key with auto increment nature

    # This function is used to provide the url to which we need to redirect, after filling the form
    def get_absolute_url(self):
        return reverse('Rhythmica:albumDetails', kwargs={'album_id': self.id})
    # We need to send the url where we need to redirect, and the parameters which are expected

    def __str__(self):
        return self.albumTitle + "-" + self.artist

    class Meta:
        unique_together = ('albumTitle', 'user')


# This table will store the mapping of a song in different albums according to users
class AlbumSongMap(models.Model):

    # Foreign keys of both related entities
    album = models.ForeignKey(Album, verbose_name="Album", on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    is_del = models.BooleanField(verbose_name="Is Deleted", default=False)
    song_title = models.CharField(max_length=100, verbose_name="Rename This Song To", null=True)
    title_change = models.BooleanField(default=False, verbose_name="Change Song Title")
    is_fav = models.BooleanField(default=False, verbose_name="Favorite")
    logo_change = models.BooleanField(default=False, verbose_name="Song Logo Changed")
    song_logo = models.ImageField(verbose_name="New Logo", null=True)
