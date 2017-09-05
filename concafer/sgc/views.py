from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout


@login_required
def home(request):
    return render(request, 'core/home.html')


def LogOut(request):
	logout(request)
	return render(request, 'core/home.html')

	