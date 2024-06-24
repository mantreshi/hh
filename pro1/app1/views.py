from django.shortcuts import render,redirect
from .forms import PersonForm
from .models import Person
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.



def hview(request):
    return render(request,'app1/home.html',{})


@login_required(login_url='/a2/lv/')
def pview(request):
    form = PersonForm()
    if request.method=="POST":
        form=PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("DATA SAVED!!!!")


    return render(request,'app1/per_form.html',{'form':form})


@login_required(login_url='/a2/lv/')
def sview(request):
    per = Person.objects.all()
    print(per)
    return render(request,'app1/show.html',{'obj':per})


def updateview(request,pk):
    obj = Person.objects.get(pid=pk)

    form  = PersonForm(instance=obj)
    if request.method=="POST":
        form = PersonForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("/a1/sv/")
    return render(request,"app1/per_form.html",{"form":form})





def deleteview(request,x):
    #obj = Person.objects.get(pid=x)
    #obj.delete()
    #return redirect('/a1/sv/')
##################################confirm page###############
    obj = Person.objects.get(pid=x)
    if request.method=="POST":
        obj.delete()
        return redirect('/a1/sv/')
    return render(request,"app1/success.html",{"obj":obj})









