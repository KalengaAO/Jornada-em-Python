from django.shortcuts import render, redirect

def	login(request):
	return render(request, "user/logo.html")

def logout(request):
	logout(request)
	return redirect("base:index")
