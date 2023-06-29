from django import forms
from .models import Profile


class ProfileForm(forms.Form):
    image = forms.ImageField(required=False)
    name = forms.CharField(max_length=32, label='Name')

    def clean(self):
        self.cleaned_data = super().clean()
        image = self.cleaned_data.get('image')
        if not image:
            self.cleaned_data['image'] = 'uploads/profile_pics/default/angel_kitty.png'

    def signup(self, request, user):
        user.save()
        profile = Profile()
        profile.user = user
        profile.image = self.cleaned_data.get('image')
        profile.name = self.cleaned_data['name']
        profile.save()
