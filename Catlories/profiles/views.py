import random
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic import UpdateView
from .models import Profile
from django.shortcuts import render
from django.views import View


class ProfileView(View):
    def get(self, request, username, *args, **kwargs):
        context = {}
        user = User.objects.get(username=username)
        profile = user.profile
        context['username'] = user.username
        context['name'] = profile.name
        context['image'] = profile.image.url
        context['sex'] = profile.sex
        context['birth_date'] = profile.birth_date
        context['weight_kg'] = profile.weight_kg
        context['height_cm'] = profile.height_cm
        context['activity_level'] = profile.activity_level
        context['goal'] = profile.goal
        return render(request, 'profiles/profile.html', context)


class UpdateProfile(UpdateView):
    model = Profile
    fields = ['name', 'image']
    template_name = 'profiles/update_profile.html'

    def form_valid(self, form):
        if not form.instance.image:
            form.instance.image = f"uploads/profile_pics/default/{random.choice(['bob.png', 'crabs.png', 'patrick.png', 'squid.png'])}"
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('profile', kwargs={'username': self.object.user.username})
