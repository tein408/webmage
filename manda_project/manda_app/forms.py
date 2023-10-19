from django import forms
from .models import Feed

class FeedForm(forms.ModelForm):
    class Meta:
        model = Feed
        fields = ['cont_id', 'main_id', 'sub_id', 'feed_contents', 'feed_image', 'feed_hash']