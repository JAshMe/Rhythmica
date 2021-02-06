""" 
    Author: JAshMe
    CSE, MNNIT Allahabad
 """

from django import forms
from django.forms import models, ValidationError
from .models import Album, Song
from django.core.exceptions import NON_FIELD_ERRORS
from django.db import IntegrityError


class AddAlbumForm(models.ModelForm):

    class Meta:
        model = Album
        fields = ('artist', 'albumTitle', 'genre', 'albumLogo')
        widgets = {
            'artist': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'artist',
                'placeholder': 'Album Artist',
                'required': 'required',
                'autofocus': 'autofocus',
            }),
            'albumTitle': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'title',
                'placeholder': 'Album Title',
                'required': 'required',
            }),
            'genre': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'genre',
                'placeholder': 'Album Genre',
            }),
            'albumLogo': forms.FileInput(attrs={
                'class': 'custom-file-input',
                'id': 'album-logo',
            }),
        }

        # These error messages are shown whenever exception regarding model structure is thrown during its validation
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "This Album already exists in your collection!!"
            }
        }


class AddSongForm(models.ModelForm):

    class Meta:
        model = Song
        fields = ('songUrl', 'songLogo', )

        widgets = {
            'songUrl': forms.FileInput(attrs={
                'class': "custom-file-input",
                'id': "song",

            }),
            'songLogo': forms.FileInput(attrs={
                'class': "custom-file-input",
                'id': 'songLogo',
            })
        }

