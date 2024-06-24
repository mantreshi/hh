from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse

# Create your views here.
def signview(request):
    form = UserCreationForm()
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/a1/sv/")
    return render(request,"authapp/signup.html",{'form':form})


def loginview(request):
    if request.method=="POST":
        u = request.POST.get("unm")
        p = request.POST.get("pwd")
        print(u,p)
        user = authenticate(username=u,password=p)
        print(user)
        if user!=None:
            login(request,user)
    return render(request,"authapp/login.html",{})



def logoutview(request):
    logout(request)
    return redirect("/a2/lv/")