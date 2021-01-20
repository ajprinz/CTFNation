from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.db import models
from django.contrib.auth.models import User
from dashboard.models import Profile
from channels import Group
from django.shortcuts import redirect
from . import queue
import sweetify


# Create your views here.

@login_required
def home(request):
    context = {"dashboard_page": "active", "title": "Dashboard"}
    return render(request, 'dashboard/dashboard.html', context)


@login_required
def matchmaking(request):
    context = {"matchmaking_page": "active", "title": "Matchmaking"}
    return render(request, 'dashboard/matchmaking.html', context)


# Matchmaking request after submit button "Find Players" is clicked => Lobby
# Check for the request
@login_required
def lobby(request):
    context = {"matchmaking_page": "active", "title": "Matchmaking"}
    return render(request, 'dashboard/lobby.html', context)


@login_required
def game(request):
    context = {"matchmaking_page": "active", "title": "Matchmaking"}
    return render(request, 'dashboard/game.html', context)


@login_required
def profile(request):
    if request.method == 'POST':

        # Update user.profile.xp
        x = Profile.objects.filter(xp__isnull=False).first()
        x.xp += 1
        x.save()
        # Update user.profile.wins
        w = Profile.objects.filter(wins__isnull=False).first()
        w.wins += 1
        w.save()
        # Update user.profile.wlratio
        wlr = Profile.objects.filter(wins__isnull=False, losses__isnull=False, wlratio__isnull=False).first()
        if wlr.losses == 0: # avoid dividing by zero
            wlr.wlratio = wlr.wins
            wlr.save()
        else:
            wlr.wlratio = wlr.wins/wlr.losses
            wlr.save()
        # Update user.profile.kdratio
        kdr = Profile.objects.filter(kills__isnull=False, deaths__isnull=False, kdratio__isnull=False).first()
        if kdr.deaths == 0: # avoid dividing by zero
            kdr.kdratio = kdr.kills
            kdr.save()
        else:
            kdr.kdratio = kdr.kills/kdr.deaths
            kdr.save()


    context = {"profile_page": "active", "title": "Profile"}
    return render(request, 'dashboard/profile.html', context)


@login_required
def settings(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            # message.success(request, f'Your account has been updated.')
            return redirect('settings')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        "profile_page": "active",
        "title": "Settings",
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'dashboard/settings.html', context)


@login_required
def campaign(request):
    context = {"campaign_page": "active", "title": "Campaign"}
    return render(request, 'dashboard/campaign.html', context)


@login_required
def customgames(request):
    context = {"customgames_page": "active", "title": "Custom Games"}
    return render(request, 'dashboard/customgames.html', context)


@login_required
def careers(request):
    context = {"careers_page": "active", "title": "Careers"}
    return render(request, 'dashboard/careers.html', context)


@login_required
def leaderboard(request):
    context = {"leaderboard_page": "active", "title": "Leaderboard"}
    return render(request, 'dashboard/leaderboard.html', context)
