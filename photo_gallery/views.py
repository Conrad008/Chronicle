from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.db.models import Q
from .models import Photo, Tag, Profile

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('photo_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def photo_list(request):
    tag_slug = request.GET.get('tag')
    photos = Photo.objects.all().order_by('-created_at')
    if tag_slug:
        photos = photos.filter(tags__name=tag_slug)
    tags = Tag.objects.all()
    return render(request, 'photo_gallery/photo_list.html', {'photos': photos, 'tags': tags, 'selected_tag': tag_slug})

def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'photo_gallery/photo_detail.html', {'photo': photo})

@login_required
def toggle_like(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    user = request.user
    if user in photo.likes.all():
        photo.likes.remove(user)
    else:
        photo.likes.add(user)
        photo.dislikes.remove(user)
    return redirect('photo_detail', pk=pk)
