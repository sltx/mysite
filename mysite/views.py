from django.shortcuts import render


def home(request):
	context = {}
	return render(request, 'base.html', context)


def happy1(request):
	context = {}
	return render(request, 'happy1.html', context)


def happy2(request):
	context = {}
	return render(request, 'happy2.html', context)