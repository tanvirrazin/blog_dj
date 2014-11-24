from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.views.generic import View
from forms import UserForm


class Login(View):

    def get(self, request):
        args = {}
        args.update(csrf(request))

        return render_to_response('site/login_form.html', args)

    def post(self, request, **kwargs):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/blog/')
        else:
            return HttpResponseRedirect('/login/')


class Logout(View):

    def get(self, request):
        auth.logout(request)
        return HttpResponseRedirect('/blog/')


class UserRegister(View):

    def get(self, request):
        args = {}
        args.update(csrf(request))
        args['user_form'] = UserForm()

        return render_to_response('site/user_registration.html', args)

    def post(self, request):
        user_form = UserForm(request.POST)

        if user_form.is_valid:
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/login/')
        else:
            return HttpResponseRedirect('/user-registration/')