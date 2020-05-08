from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from .models import UserDetail, UserEducation, UserSocialMedia

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('user-my-profile')
        else:
            return redirect('login-page')
    else:
        return render(request, 'user/login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        country = request.POST['country']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        username = email

        if password == password2:
            if User.objects.filter(email=email).exists():
                return redirect('login-page')
            else:
                user = User.objects.create_user(
                    username=username, password=password, first_name=first_name, last_name=last_name, email=email)
                userdetail = UserDetail(user=user, country=country)
                user.save()
                userdetail.save()
                auth.login(request, user)
                return redirect('user-my-profile')
        else:
            return redirect('login-page')
    else:
        return redirect('login-page')


def logout(request):
    auth.logout(request)
    return redirect('home-page')


@login_required(login_url='login-page')
def myProfile(request):
    # print('user id', request.user.id)
    # user_education = UserEducation.objects.all()
    # for education in user_education:
    #     print('education', education)
    user_education = UserEducation.objects.filter(user_id=request.user.id)
    user_social_medias = UserSocialMedia.objects.filter(
        user_id=request.user.id)
    context = {
        'educations': user_education,
        'user_social_medias': user_social_medias,
    }
    return render(request, 'user/my-profile.html', context)
