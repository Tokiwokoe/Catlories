from django import forms
from .models import Profile, Sex, ActivityLevel, Goal


class ProfileForm(forms.Form):
    image = forms.ImageField(required=False, label='Аватар')
    name = forms.CharField(max_length=32, label='Имя')
    sex = forms.ModelChoiceField(queryset=Sex.objects.all(), label='Пол')
    birth_date = forms.DateField(label='Дата рождения')
    weight_kg = forms.FloatField(label='Вес (кг)')
    height_cm = forms.IntegerField(label='Рост (см)')
    activity_level = forms.ModelChoiceField(queryset=ActivityLevel.objects.all(), label='Уровень активности')
    goal = forms.ModelChoiceField(queryset=Goal.objects.all(), label='Цель')

    def clean(self):
        self.cleaned_data = super().clean()
        image = self.cleaned_data.get('image')
        if not image:
            self.cleaned_data['image'] = 'profile_pics/default/angel_kitty.png'
        return self.cleaned_data

    def signup(self, request, user):
        user.save()
        profile = Profile()
        profile.user = user
        profile.image = self.cleaned_data['image']
        profile.name = self.cleaned_data['name']
        profile.sex = self.cleaned_data['sex']
        profile.birth_date = self.cleaned_data['birth_date']
        profile.weight_kg = self.cleaned_data['weight_kg']
        profile.height_cm = self.cleaned_data['height_cm']
        profile.activity_level = self.cleaned_data['activity_level']
        profile.goal = self.cleaned_data['goal']
        profile.save()
