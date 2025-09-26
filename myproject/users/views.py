from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import UserProfileForm

def user_list(request):
    users = UserProfile.objects.all()
    return render(request, "users/user_list.html", {"users": users})


def create_userprofile(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # başarılı olunca yönlendirme
    else:
        form = UserProfileForm()

    return render(request, 'users/create_userprofile.html', {'form': form})
