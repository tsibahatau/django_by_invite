from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

from django.template.loader import render_to_string
from django.core.mail import send_mail
from invites.models import Invite, UserProfile


def post_list(request):
    return render(request, 'invites/post_list.html', {})

def create_user(request):
    if request and request.GET.get('invite'):
        uiid = request.GET['invite']
        invite = Invite.objects.get(key=uiid)
        if invite and not invite.is_used:
            user =  User.objects.create_user(username=invite.email,
                                     email=invite.email,
                                     password='supermegapassword')
            profile = UserProfile.objects.create(user=user,invite_used=invite)
            invite.is_used = True
            invite.save()
            print(profile.user.email)
            return render(request,'invites/user_created_succesfully.html')
    return render(request,'invites/user_creating_wrong.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request,'invites/logout_page.html')
    if request.method == 'GET':
        if request.user.is_authenticated():
            return render(request,'invites/logout_page.html')
    return render(request,'invites/login_page.html')

@login_required
def user_logout(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            logout(request)
            return render(request,'invites/login_page.html')